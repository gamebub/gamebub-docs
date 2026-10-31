#!/usr/bin/env python3

import json
import os
import re
import urllib.request
from urllib.error import HTTPError, URLError

TAG = re.compile(r"^v(\d+)\.(\d+)\.(\d+)(?:-beta(\d+))?$")  # v1.2.3, v1.2.3-beta4
NOESCAPE = re.compile(r"[A-Za-z0-9 ]")
OUTPUT = "docs/developing-cores/community-cores.md"


def main():
    token = os.environ["GH_TOKEN"]
    infos = []

    repos = api("search/repositories?q=topic:game-bub-core", token=token)
    assert not repos["incomplete_results"]
    repos = set(repo["full_name"] for repo in repos["items"])

    # Temporary until game-bub-core topic is applied
    repos.add("danifunker/MacLC_GameBub")
    repos.add("neutralinsomniac/gamebub")

    for repo in sorted(repos):
        print(repo)

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

        ident = repo
        system = author = license = ""
        for ref in [latest, latest_beta, "main"]:
            if not ref:
                continue
            metadata = {}
            core_json = api(
                f"repos/{repo}/contents/metadata/core.json?ref={ref}",
                token=token,
                headers={"Accept": "application/vnd.github.raw+json"},
            )
            if not core_json:
                continue
            if isinstance(core_json, dict) and isinstance(
                core_json.get("metadata"), dict
            ):
                metadata = core_json["metadata"]
            ident = str(metadata.get("id", repo))
            system = str(metadata.get("name", ""))
            author = str(metadata.get("author", ""))
            license = str(metadata.get("license", ""))
            break

        base = f"https://github.com/{repo}"
        link = f"[{md_escape(ident)}]({base})"
        latest_link = latest_beta_link = ""
        if latest:
            latest_link = f"[{latest}]({base}/releases/tag/{latest})"
        if latest_beta:
            latest_beta_link = f"[{latest_beta}]({base}/releases/tag/{latest_beta})"
        infos.append(
            (
                link,
                md_escape(system),
                md_escape(author),
                latest_link,
                latest_beta_link,
                md_escape(license),
            )
        )

    infos.sort(key=lambda row: row[0].lower())
    with open(OUTPUT, "r") as f:
        content = f.read()
        header, content = content.split("<!-- BEGIN AUTOGEN -->")
        header = header.strip("\n")
        content, footer = content.split("<!-- END AUTOGEN -->")
        footer = footer.strip("\n")
    with open(OUTPUT, "w") as f:
        print(header, file=f)
        print(file=f)
        print("<!-- BEGIN AUTOGEN -->", file=f)
        print("| Core | System | Author | Release | Beta | License |", file=f)
        print("| :--- | :--- | :--- | :--- | :--- | :--- |", file=f)
        for info in infos:
            print("|", " | ".join(info), "|", file=f)
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


if __name__ == "__main__":
    main()
