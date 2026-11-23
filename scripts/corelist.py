#!/usr/bin/env python3

import json
import os
import re
import sys
import urllib.request
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlsplit, urlunsplit

TAG = re.compile(r"^v(\d+)\.(\d+)\.(\d+)(?:-beta(\d+))?$")  # v1.2.3, v1.2.3-beta4
NOESCAPE = re.compile(r"[ A-Za-z0-9./]")
OUTPUT_MD = "docs/developing-cores/community-cores.md"
OUTPUT_JSON = "docs/developing-cores/community-cores.json"


def main():
    token = os.environ["GH_TOKEN"]
    infos = {}

    repos = api("search/repositories?q=topic:game-bub-core", token=token)
    assert not repos["incomplete_results"]
    repos = set(repo["full_name"] for repo in repos["items"])

    # Temporary until game-bub-core topic is applied
    repos.add("danifunker/MacLC_GameBub")
    repos.add("neutralinsomniac/gamebub")

    for repo in sorted(repos, key=lambda repo: repo.lower()):
        print(repo, file=sys.stderr)

        latest = None
        latest_beta = None
        releases = api(f"repos/{repo}/releases", token=token)
        if not releases:
            continue
        for release in releases:
            m = TAG.match(release["tag_name"])
            if not m:
                continue
            major, minor, patch, beta = [(int(x) if x else None) for x in m.groups()]
            if beta is None:
                if (not latest) or ((major, minor, patch) > latest):
                    latest = (major, minor, patch)
            else:
                if (not latest_beta) or ((major, minor, patch, beta) > latest_beta):
                    latest_beta = (major, minor, patch, beta)

        if latest:
            major, minor, patch = latest
            latest = f"v{major}.{minor}.{patch}"
        if latest_beta:
            major, minor, patch, beta = latest_beta
            latest_beta = f"v{major}.{minor}.{patch}-beta{beta}"

        metadata = {}
        for ref in [latest, latest_beta, "main"]:
            if not ref:
                continue
            core_json = api(
                f"repos/{repo}/contents/metadata/core.json?ref={ref}",
                token=token,
                headers={"Accept": "application/vnd.github.raw+json"},
            )
            if (
                core_json
                and isinstance(core_json, dict)
                and isinstance(core_json.get("metadata"), dict)
            ):
                metadata = core_json["metadata"]
                break

        ident = str(metadata.get("id", repo))
        infos[repo] = {
            "id": ident,
            "latest": latest,
            "latest_beta": latest_beta,
            "metadata": metadata,
        }

    with open(OUTPUT_JSON, "r") as f:
        old_infos = json.load(f)

    with open(OUTPUT_MD, "r") as f:
        content = f.read()
        header, content = content.split("<!-- BEGIN AUTOGEN -->")
        header = header.strip("\n")
        content, footer = content.split("<!-- END AUTOGEN -->")
        footer = footer.strip("\n")

    with open(OUTPUT_JSON, "w") as f:
        json.dump(infos, f, indent="  ")
        print(file=f)

    with open(OUTPUT_MD, "w") as f:
        print(header, file=f)
        print(file=f)
        print("<!-- BEGIN AUTOGEN -->", file=f)
        print("| Core | System | Author | Release | Beta | License |", file=f)
        print("| :--- | :--- | :--- | :--- | :--- | :--- |", file=f)
        for repo, info in sorted(infos.items(), key=lambda row: row[1]["id"].lower()):
            ident = info["id"]
            latest = info["latest"]
            latest_beta = info["latest_beta"]
            metadata = info["metadata"]
            base = f"https://github.com/{repo}"
            url = str(metadata.get("url", base))

            if repo not in old_infos:
                changed = "added"
            elif info != old_infos[repo]:
                changed = "updated"
            else:
                changed = None
            if changed:
                if latest or latest_beta:
                    print(f"* {changed}: {ident} ({latest or latest_beta})")
                else:
                    print(f"* {changed}: {ident}")

            print(
                "|",
                " | ".join(
                    [
                        md_item(ident, link=url),
                        md_item(str(metadata.get("name", ""))),
                        md_item(str(metadata.get("author", ""))),
                        md_item(latest, link=f"{base}/releases/tag/{latest}"),
                        md_item(latest_beta, link=f"{base}/releases/tag/{latest_beta}"),
                        md_item(str(metadata.get("license", ""))),
                    ]
                ),
                "|",
                file=f,
            )
        print("<!-- END AUTOGEN -->", file=f)
        print(footer, file=f)


def api(path, *, token, headers={}):
    merged_headers = {
        "Authorization": f"Bearer {token}",
        "User-Agent": "gamebub/gamebub-docs",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2026-03-10",
    }
    merged_headers.update(headers)
    req = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers=merged_headers,
    )
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
    except json.decoder.JSONDecodeError:
        return None


def md_escape(s):
    chars = []
    for ch in s:
        if s == "\n":
            chars.append("<br/>")
        elif NOESCAPE.match(ch):
            chars.append(ch)
        else:
            chars.append(f"&#{ord(ch)};")
    return "".join(chars)


def md_item(text, *, link=None):
    if not text:
        return ""
    text = md_escape(text)
    if link:
        link = urlsplit(link)
        if link.scheme not in ["http", "https"]:
            return text
        link = urlunsplit(
            (
                link.scheme,
                link.netloc,
                quote(link.path, safe="/%"),
                quote(link.query, safe="=&%"),
                quote(link.fragment, safe="%"),
            )
        )
        return f"[{text}]({link})"
    return text


if __name__ == "__main__":
    main()
