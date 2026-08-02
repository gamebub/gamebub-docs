# Copyrights & Licenses

<style>
	.md-typeset ul li {
		margin-bottom: 0;
	}
</style>

Game Bub is open source:

* The firmware is licensed under [GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
* The gateware and hardware are licensed under [CERN-OHL-S](https://choosealicense.com/licenses/cern-ohl-s-2.0/)

You can find source code [on GitHub](https://github.com/elipsitz/gamebub).

**Game Bub**™ is a trademark of Second Bedroom LLC.

At a high level, this means that you can copy, share, and modify the source code, as long as you provide proper attribution and share your source code / design files with the same license. However, this does not mean that you can use the "Game Bub" name and logo for your product without permission.

## Open Source Components

Game Bub is also built on top of numerous pieces of open-source software.

### Handheld Firmware

* [esp-idf](https://github.com/espressif/esp-idf): Copyright (c) 2015-2023 Espressif Systems, licensed under the [Apache License 2.0](https://github.com/espressif/esp-idf/blob/master/LICENSE). Licenses of subcomponents [can be found here](https://docs.espressif.com/projects/esp-idf/en/v5.4.3/esp32s3/COPYRIGHT.html).
* [tinyusb](https://github.com/hathach/tinyusb/): Copyright (c) 2012-2026 Ha Thach (tinyusb.org), licensed under the [MIT license](https://github.com/hathach/tinyusb/blob/master/LICENSE)

<!-- begin cargo dependencies (handheld) -->
* [adler2](https://github.com/oyvindln/adler2): Licensed under 0BSD OR Apache-2.0 OR MIT
* [aho-corasick](https://github.com/BurntSushi/aho-corasick): Licensed under MIT OR Unlicense
* [aligned](https://github.com/rust-embedded-community/aligned): Licensed under Apache-2.0 OR MIT
* [aligned-vec](https://github.com/sarah-ek/aligned-vec/): Licensed under MIT
* [allocator-api2](https://github.com/zakarumych/allocator-api2): Licensed under Apache-2.0 OR MIT
* [anyhow](https://github.com/dtolnay/anyhow): Licensed under Apache-2.0 OR MIT
* [arg_enum_proc_macro](https://github.com/lu-zero/arg_enum_proc_macro): Licensed under MIT
* [arrayref](https://github.com/droundy/arrayref): Licensed under BSD-2-Clause
* [arrayvec](https://github.com/bluss/arrayvec): Licensed under Apache-2.0 OR MIT
* [as-slice](https://github.com/japaric/as-slice): Licensed under Apache-2.0 OR MIT
* [async-broadcast](https://github.com/smol-rs/async-broadcast): Licensed under Apache-2.0 OR MIT
* [async-channel](https://github.com/smol-rs/async-channel): Licensed under Apache-2.0 OR MIT
* [async-executor](https://github.com/smol-rs/async-executor): Licensed under Apache-2.0 OR MIT
* [async-io](https://github.com/smol-rs/async-io): Licensed under Apache-2.0 OR MIT
* [async-lock](https://github.com/smol-rs/async-lock): Licensed under Apache-2.0 OR MIT
* [async-process](https://github.com/smol-rs/async-process): Licensed under Apache-2.0 OR MIT
* [async-recursion](https://github.com/dcchut/async-recursion): Licensed under Apache-2.0 OR MIT
* [async-signal](https://github.com/smol-rs/async-signal): Licensed under Apache-2.0 OR MIT
* [async-task](https://github.com/smol-rs/async-task): Licensed under Apache-2.0 OR MIT
* [async-trait](https://github.com/dtolnay/async-trait): Licensed under Apache-2.0 OR MIT
* [atomic-waker](https://github.com/smol-rs/atomic-waker): Licensed under Apache-2.0 OR MIT
* [auto_enums](https://github.com/taiki-e/auto_enums): Licensed under Apache-2.0 OR MIT
* [autocfg](https://github.com/cuviper/autocfg): Licensed under Apache-2.0 OR MIT
* [av-scenechange](https://github.com/rust-av/av-scenechange): Licensed under MIT
* [av1-grain](https://github.com/rust-av/av1-grain): Licensed under BSD-2-Clause
* [avif-serialize](https://github.com/kornelski/avif-serialize): Licensed under BSD-3-Clause
* [base64](https://github.com/marshallpierce/rust-base64): Licensed under Apache-2.0 OR MIT
* [bincode](https://github.com/bincode-org/bincode): Licensed under MIT
* [bindgen](https://github.com/rust-lang/rust-bindgen): Licensed under BSD-3-Clause
* [bit_field](https://github.com/phil-opp/rust-bit-field): Licensed under Apache-2.0 OR MIT
* [bitflags](https://github.com/bitflags/bitflags): Licensed under Apache-2.0 OR MIT
* [bitstream-io](https://github.com/tuffy/bitstream-io): Licensed under Apache-2.0 OR MIT
* [blocking](https://github.com/smol-rs/blocking): Licensed under Apache-2.0 OR MIT
* [borsh](https://github.com/near/borsh-rs): Licensed under Apache-2.0 OR MIT
* [bstr](https://github.com/BurntSushi/bstr): Licensed under Apache-2.0 OR MIT
* [build-time](https://github.com/AlephAlpha/build-time): Licensed under MIT
* [built](https://github.com/lukaslueg/built): Licensed under MIT
* [bumpalo](https://github.com/fitzgen/bumpalo): Licensed under Apache-2.0 OR MIT
* [by_address](https://github.com/mbrubeck/by_address): Licensed under Apache-2.0 OR MIT
* [bytemuck](https://github.com/Lokathor/bytemuck): Licensed under Apache-2.0 OR MIT OR Zlib
* [bytemuck_derive](https://github.com/Lokathor/bytemuck): Licensed under Apache-2.0 OR MIT OR Zlib
* [byteorder](https://github.com/BurntSushi/byteorder): Licensed under MIT OR Unlicense
* [byteorder-lite](https://github.com/image-rs/byteorder-lite): Licensed under MIT OR Unlicense
* [bytes](https://github.com/tokio-rs/bytes): Licensed under MIT
* [calloop](https://github.com/Smithay/calloop): Licensed under MIT
* [camino](https://github.com/camino-rs/camino): Licensed under Apache-2.0 OR MIT
* [cargo-platform](https://github.com/rust-lang/cargo): Licensed under Apache-2.0 OR MIT
* [cargo_metadata](https://github.com/oli-obk/cargo_metadata): Licensed under MIT
* [cc](https://github.com/rust-lang/cc-rs): Licensed under Apache-2.0 OR MIT
* [cexpr](https://github.com/jethrogb/rust-cexpr): Licensed under Apache-2.0 OR MIT
* [cfg-if](https://github.com/rust-lang/cfg-if): Licensed under Apache-2.0 OR MIT
* [cfg_aliases](https://github.com/katharostech/cfg_aliases): Licensed under MIT
* [chrono](https://github.com/chronotope/chrono): Licensed under Apache-2.0 OR MIT
* [clang-sys](https://github.com/KyleMayes/clang-sys): Licensed under Apache-2.0
* [clru](https://github.com/marmeladema/clru-rs): Licensed under MIT
* [cmake](https://github.com/rust-lang/cmake-rs): Licensed under Apache-2.0 OR MIT
* [cobs](https://github.com/jamesmunns/cobs.rs): Licensed under Apache-2.0 OR MIT
* [codemap](https://github.com/kevinmehall/codemap): Licensed under Apache-2.0 OR MIT
* [codemap-diagnostic](https://github.com/kevinmehall/codemap-diagnostic): Licensed under Apache-2.0 OR MIT
* [color_quant](https://github.com/image-rs/color_quant.git): Licensed under MIT
* [concurrent-queue](https://github.com/smol-rs/concurrent-queue): Licensed under Apache-2.0 OR MIT
* [const-field-offset](https://github.com/slint-ui/slint): Licensed under Apache-2.0 OR MIT
* [const-field-offset-macro](https://github.com/slint-ui/slint): Licensed under Apache-2.0 OR MIT
* [const_format](https://github.com/rodrimati1992/const_format_crates/): Licensed under Zlib
* [const_format_proc_macros](https://github.com/rodrimati1992/const_format_crates/): Licensed under Zlib
* [convert_case](https://github.com/rutrum/convert-case): Licensed under MIT
* [copypasta](https://github.com/alacritty/copypasta): Licensed under Apache-2.0 OR MIT
* [core_maths](https://github.com/robertbastian/core_maths): Licensed under MIT
* [countme](https://github.com/matklad/countme): Licensed under Apache-2.0 OR MIT
* [crc32fast](https://github.com/srijs/rust-crc32fast): Licensed under Apache-2.0 OR MIT
* [critical-section](https://github.com/rust-embedded/critical-section): Licensed under Apache-2.0 OR MIT
* [crossbeam-deque](https://github.com/crossbeam-rs/crossbeam): Licensed under Apache-2.0 OR MIT
* [crossbeam-epoch](https://github.com/crossbeam-rs/crossbeam): Licensed under Apache-2.0 OR MIT
* [crossbeam-utils](https://github.com/crossbeam-rs/crossbeam): Licensed under Apache-2.0 OR MIT
* [cursor-icon](https://github.com/rust-windowing/cursor-icon): Licensed under Apache-2.0 OR MIT OR Zlib
* [cvt](https://github.com/marmistrz/cvt): Licensed under Apache-2.0
* [darling](https://github.com/TedDriggs/darling): Licensed under MIT
* [darling_core](https://github.com/TedDriggs/darling): Licensed under MIT
* [darling_macro](https://github.com/TedDriggs/darling): Licensed under MIT
* [data-url](https://github.com/servo/rust-url): Licensed under Apache-2.0 OR MIT
* [defmt](https://github.com/knurling-rs/defmt): Licensed under Apache-2.0 OR MIT
* [defmt-macros](https://github.com/knurling-rs/defmt): Licensed under Apache-2.0 OR MIT
* [defmt-parser](https://github.com/knurling-rs/defmt): Licensed under Apache-2.0 OR MIT
* [deranged](https://github.com/jhpratt/deranged): Licensed under Apache-2.0 OR MIT
* [derive_more](https://github.com/JelteF/derive_more): Licensed under MIT
* [derive_more-impl](https://github.com/JelteF/derive_more): Licensed under MIT
* [derive_utils](https://github.com/taiki-e/derive_utils): Licensed under Apache-2.0 OR MIT
* [displaydoc](https://github.com/yaahc/displaydoc): Licensed under Apache-2.0 OR MIT
* [dlib](https://github.com/elinorbgr/dlib): Licensed under MIT
* [document-features](https://github.com/slint-ui/document-features): Licensed under Apache-2.0 OR MIT
* [dpi](https://github.com/rust-windowing/winit): Licensed under Apache-2.0 AND MIT
* [either](https://github.com/rayon-rs/either): Licensed under Apache-2.0 OR MIT
* [embassy-futures](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-sync](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-time-driver](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embedded-can](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-hal](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-hal-async](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-hal-bus](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-hal-nb](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-io](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-io-async](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-svc](https://github.com/esp-rs/embedded-svc): Licensed under Apache-2.0 OR MIT
* [embuild](https://github.com/ivmarkov/embuild): Licensed under Apache-2.0 OR MIT
* [endi](https://github.com/zeenix/endi): Licensed under MIT
* [enum-map](https://codeberg.org/xfix/enum-map): Licensed under Apache-2.0 OR MIT
* [enum-map-derive](https://codeberg.org/xfix/enum-map): Licensed under Apache-2.0 OR MIT
* [enumflags2](https://github.com/meithecatte/enumflags2): Licensed under Apache-2.0 OR MIT
* [enumflags2_derive](https://github.com/meithecatte/enumflags2): Licensed under Apache-2.0 OR MIT
* [enumset](https://github.com/Lymia/enumset): Licensed under Apache-2.0 OR MIT
* [enumset_derive](https://github.com/Lymia/enumset): Licensed under Apache-2.0 OR MIT
* [envy](https://github.com/softprops/envy): Licensed under MIT
* [equator](https://github.com/sarah-ek/equator/): Licensed under MIT
* [equator-macro](https://github.com/sarah-ek/equator/): Licensed under MIT
* [equivalent](https://github.com/indexmap-rs/equivalent): Licensed under Apache-2.0 OR MIT
* [errno](https://github.com/lambda-fairy/rust-errno): Licensed under Apache-2.0 OR MIT
* [esp-idf-hal](https://github.com/esp-rs/esp-idf-hal): Licensed under Apache-2.0 OR MIT
* [esp-idf-svc](https://github.com/esp-rs/esp-idf-svc): Licensed under Apache-2.0 OR MIT
* [esp-idf-sys](https://github.com/esp-rs/esp-idf-sys): Licensed under Apache-2.0 OR MIT
* [euclid](https://github.com/servo/euclid): Licensed under Apache-2.0 OR MIT
* [event-listener](https://github.com/smol-rs/event-listener): Licensed under Apache-2.0 OR MIT
* [event-listener-strategy](https://github.com/smol-rs/event-listener-strategy): Licensed under Apache-2.0 OR MIT
* [exr](https://github.com/johannesvollmer/exrs): Licensed under BSD-3-Clause
* [fastrand](https://github.com/smol-rs/fastrand): Licensed under Apache-2.0 OR MIT
* [fax](https://github.com/pdf-rs/fax): Licensed under MIT
* [fdeflate](https://github.com/image-rs/fdeflate): Licensed under Apache-2.0 OR MIT
* [field-offset](https://github.com/Diggsey/rust-field-offset): Licensed under Apache-2.0 OR MIT
* [filetime](https://github.com/alexcrichton/filetime): Licensed under Apache-2.0 OR MIT
* [find-msvc-tools](https://github.com/rust-lang/cc-rs): Licensed under Apache-2.0 OR MIT
* [flate2](https://github.com/rust-lang/flate2-rs): Licensed under Apache-2.0 OR MIT
* [float-cmp](https://github.com/mikedilger/float-cmp): Licensed under MIT
* [fnv](https://github.com/servo/rust-fnv): Licensed under Apache-2.0 OR MIT
* [foldhash](https://github.com/orlp/foldhash): Licensed under Zlib
* [fontconfig-parser](https://github.com/Riey/fontconfig-parser): Licensed under MIT
* [fontdb](https://github.com/RazrFalcon/fontdb): Licensed under MIT
* [fontdue](https://github.com/mooman219/fontdue): Licensed under Apache-2.0 OR MIT OR Zlib
* [form_urlencoded](https://github.com/servo/rust-url): Licensed under Apache-2.0 OR MIT
* [fs_at](https://github.com/rbtcollins/fs_at.git): Licensed under Apache-2.0
* [futures](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-channel](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-core](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-executor](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-io](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-lite](https://github.com/smol-rs/futures-lite): Licensed under Apache-2.0 OR MIT
* [futures-macro](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-sink](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-task](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-util](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [getrandom](https://github.com/rust-random/getrandom): Licensed under Apache-2.0 OR MIT
* [gif](https://github.com/image-rs/image-gif): Licensed under Apache-2.0 OR MIT
* [glob](https://github.com/rust-lang/glob): Licensed under Apache-2.0 OR MIT
* [globset](https://github.com/BurntSushi/ripgrep/tree/master/crates/globset): Licensed under MIT OR Unlicense
* [globwalk](https://github.com/gilnaa/globwalk): Licensed under MIT
* [half](https://github.com/VoidStarKat/half-rs): Licensed under Apache-2.0 OR MIT
* [hash32](https://github.com/japaric/hash32): Licensed under Apache-2.0 OR MIT
* [hashbrown](https://github.com/rust-lang/hashbrown): Licensed under Apache-2.0 OR MIT
* [heapless](https://github.com/rust-embedded/heapless): Licensed under Apache-2.0 OR MIT
* [heck](https://github.com/withoutboats/heck): Licensed under Apache-2.0 OR MIT
* [hex](https://github.com/KokaKiwi/rust-hex): Licensed under Apache-2.0 OR MIT
* [home](https://github.com/rust-lang/cargo): Licensed under Apache-2.0 OR MIT
* [i-slint-backend-selector](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [i-slint-backend-winit](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [i-slint-common](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [i-slint-compiler](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [i-slint-core](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [i-slint-core-macros](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [iana-time-zone](https://github.com/strawlab/iana-time-zone): Licensed under Apache-2.0 OR MIT
* [icu_collections](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [icu_locale_core](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [icu_normalizer](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [icu_normalizer_data](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [icu_properties](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [icu_properties_data](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [icu_provider](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [ident_case](https://github.com/TedDriggs/ident_case): Licensed under Apache-2.0 OR MIT
* [idna](https://github.com/servo/rust-url/): Licensed under Apache-2.0 OR MIT
* [idna_adapter](https://github.com/hsivonen/idna_adapter): Licensed under Apache-2.0 OR MIT
* [ignore](https://github.com/BurntSushi/ripgrep/tree/master/crates/ignore): Licensed under MIT OR Unlicense
* [image](https://github.com/image-rs/image): Licensed under Apache-2.0 OR MIT
* [image-webp](https://github.com/image-rs/image-webp): Licensed under Apache-2.0 OR MIT
* [imagesize](https://github.com/Roughsketch/imagesize): Licensed under MIT
* [imgref](https://github.com/kornelski/imgref): Licensed under Apache-2.0 OR CC0-1.0
* [indexmap](https://github.com/indexmap-rs/indexmap): Licensed under Apache-2.0 OR MIT
* [integer-sqrt](https://github.com/derekdreery/integer-sqrt-rs): Licensed under Apache-2.0 OR MIT
* [itertools](https://github.com/rust-itertools/itertools): Licensed under Apache-2.0 OR MIT
* [itoa](https://github.com/dtolnay/itoa): Licensed under Apache-2.0 OR MIT
* [jobserver](https://github.com/rust-lang/jobserver-rs): Licensed under Apache-2.0 OR MIT
* [konst](https://github.com/rodrimati1992/konst/): Licensed under Zlib
* [konst_macro_rules](https://github.com/rodrimati1992/konst/): Licensed under Zlib
* [kurbo](https://github.com/linebender/kurbo): Licensed under Apache-2.0 OR MIT
* [lebe](https://github.com/johannesvollmer/lebe): Licensed under BSD-3-Clause
* [libc](https://github.com/rust-lang/libc): Licensed under Apache-2.0 OR MIT
* [libloading](https://github.com/nagisa/rust_libloading/): Licensed under ISC
* [libm](https://github.com/rust-lang/compiler-builtins): Licensed under MIT
* [linereader](https://github.com/Freaky/rust-linereader.git): Licensed under MIT
* [linked-hash-map](https://github.com/contain-rs/linked-hash-map): Licensed under Apache-2.0 OR MIT
* [linked_hash_set](https://github.com/alexheretic/linked-hash-set): Licensed under Apache-2.0
* [litemap](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [litrs](https://github.com/LukasKalbertodt/litrs): Licensed under Apache-2.0 OR MIT
* [log](https://github.com/rust-lang/log): Licensed under Apache-2.0 OR MIT
* [loop9](https://gitlab.com/kornelski/loop9.git): Licensed under MIT
* [lyon_algorithms](https://github.com/nical/lyon): Licensed under Apache-2.0 OR MIT
* [lyon_extra](https://github.com/nical/lyon): Licensed under Apache-2.0 OR MIT
* [lyon_geom](https://github.com/nical/lyon): Licensed under Apache-2.0 OR MIT
* [lyon_path](https://github.com/nical/lyon): Licensed under Apache-2.0 OR MIT
* [maybe-rayon](https://github.com/shssoichiro/maybe-rayon): Licensed under MIT
* [memchr](https://github.com/BurntSushi/memchr): Licensed under MIT OR Unlicense
* [memmap2](https://github.com/RazrFalcon/memmap2-rs): Licensed under Apache-2.0 OR MIT
* [memoffset](https://github.com/Gilnaa/memoffset): Licensed under MIT
* [minimal-lexical](https://github.com/Alexhuszagh/minimal-lexical): Licensed under Apache-2.0 OR MIT
* [miniz_oxide](https://github.com/Frommi/miniz_oxide/tree/master/miniz_oxide): Licensed under Apache-2.0 OR MIT OR Zlib
* [moxcms](https://github.com/awxkee/moxcms.git): Licensed under Apache-2.0 OR BSD-3-Clause
* [nb](https://github.com/rust-embedded/nb): Licensed under Apache-2.0 OR MIT
* [new_debug_unreachable](https://github.com/mbrubeck/rust-debug-unreachable): Licensed under MIT
* [nix](https://github.com/nix-rust/nix): Licensed under MIT
* [no_std_io2](https://github.com/wcampbell0x2a/no-std-io2): Licensed under Apache-2.0 OR MIT
* [nom](https://github.com/rust-bakery/nom): Licensed under MIT
* [noop_proc_macro](https://github.com/lu-zero/noop_proc_macro): Licensed under MIT
* [normpath](https://github.com/dylni/normpath): Licensed under Apache-2.0 OR MIT
* [num-bigint](https://github.com/rust-num/num-bigint): Licensed under Apache-2.0 OR MIT
* [num-complex](https://github.com/rust-num/num-complex): Licensed under Apache-2.0 OR MIT
* [num-conv](https://github.com/jhpratt/num-conv): Licensed under Apache-2.0 OR MIT
* [num-derive](https://github.com/rust-num/num-derive): Licensed under Apache-2.0 OR MIT
* [num-integer](https://github.com/rust-num/num-integer): Licensed under Apache-2.0 OR MIT
* [num-rational](https://github.com/rust-num/num-rational): Licensed under Apache-2.0 OR MIT
* [num-traits](https://github.com/rust-num/num-traits): Licensed under Apache-2.0 OR MIT
* [num_enum](https://github.com/illicitonion/num_enum): Licensed under Apache-2.0 OR BSD-3-Clause OR MIT
* [num_enum_derive](https://github.com/illicitonion/num_enum): Licensed under Apache-2.0 OR BSD-3-Clause OR MIT
* [once_cell](https://github.com/matklad/once_cell): Licensed under Apache-2.0 OR MIT
* [ordered-stream](https://github.com/danieldg/ordered-stream): Licensed under Apache-2.0 OR MIT
* [parking](https://github.com/smol-rs/parking): Licensed under Apache-2.0 OR MIT
* [paste](https://github.com/dtolnay/paste): Licensed under Apache-2.0 OR MIT
* [pastey](https://github.com/as1100k/pastey): Licensed under Apache-2.0 OR MIT
* [percent-encoding](https://github.com/servo/rust-url/): Licensed under Apache-2.0 OR MIT
* [pico-args](https://github.com/RazrFalcon/pico-args): Licensed under MIT
* [pin-project](https://github.com/taiki-e/pin-project): Licensed under Apache-2.0 OR MIT
* [pin-project-internal](https://github.com/taiki-e/pin-project): Licensed under Apache-2.0 OR MIT
* [pin-project-lite](https://github.com/taiki-e/pin-project-lite): Licensed under Apache-2.0 OR MIT
* [pin-utils](https://github.com/rust-lang-nursery/pin-utils): Licensed under Apache-2.0 OR MIT
* [pin-weak](https://github.com/sixtyfpsui/pin-weak): Licensed under MIT
* [piper](https://github.com/smol-rs/piper): Licensed under Apache-2.0 OR MIT
* [png](https://github.com/image-rs/image-png): Licensed under Apache-2.0 OR MIT
* [polib](https://github.com/brettdong/polib): Licensed under MIT
* [polling](https://github.com/smol-rs/polling): Licensed under Apache-2.0 OR MIT
* [portable-atomic](https://github.com/taiki-e/portable-atomic): Licensed under Apache-2.0 OR MIT
* [postcard](https://github.com/jamesmunns/postcard): Licensed under Apache-2.0 OR MIT
* [potential_utf](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [powerfmt](https://github.com/jhpratt/powerfmt): Licensed under Apache-2.0 OR MIT
* [prettyplease](https://github.com/dtolnay/prettyplease): Licensed under Apache-2.0 OR MIT
* [proc-macro-crate](https://github.com/bkchr/proc-macro-crate): Licensed under Apache-2.0 OR MIT
* [proc-macro2](https://github.com/dtolnay/proc-macro2): Licensed under Apache-2.0 OR MIT
* [profiling](https://github.com/aclysma/profiling): Licensed under Apache-2.0 OR MIT
* [profiling-procmacros](https://github.com/aclysma/profiling): Licensed under Apache-2.0 OR MIT
* [pulp](https://github.com/sarah-quinones/pulp/): Licensed under MIT
* [pulp-wasm-simd-flag](https://github.com/sarah-quinones/pulp/): Licensed under MIT
* [pxfm](https://github.com/awxkee/pxfm): Licensed under Apache-2.0 OR BSD-3-Clause
* [qoi](https://github.com/aldanor/qoi-rust): Licensed under Apache-2.0 OR MIT
* [quick-error](http://github.com/tailhook/quick-error): Licensed under Apache-2.0 OR MIT
* [quote](https://github.com/dtolnay/quote): Licensed under Apache-2.0 OR MIT
* [rav1e](https://github.com/xiph/rav1e/): Licensed under BSD-2-Clause
* [ravif](https://github.com/kornelski/cavif-rs): Licensed under BSD-3-Clause
* [raw-window-handle](https://github.com/rust-windowing/raw-window-handle): Licensed under Apache-2.0 OR MIT OR Zlib
* [rayon](https://github.com/rayon-rs/rayon): Licensed under Apache-2.0 OR MIT
* [rayon-core](https://github.com/rayon-rs/rayon): Licensed under Apache-2.0 OR MIT
* [reborrow](https://github.com/sarah-ek/reborrow/): Licensed under MIT
* [regex](https://github.com/rust-lang/regex): Licensed under Apache-2.0 OR MIT
* [regex-automata](https://github.com/rust-lang/regex): Licensed under Apache-2.0 OR MIT
* [regex-syntax](https://github.com/rust-lang/regex): Licensed under Apache-2.0 OR MIT
* [remove_dir_all](https://github.com/XAMPPRocky/remove_dir_all.git): Licensed under Apache-2.0 OR MIT
* [resvg](https://github.com/linebender/resvg): Licensed under Apache-2.0 OR MIT
* [rgb](https://github.com/kornelski/rust-rgb): Licensed under MIT
* [rowan](https://github.com/rust-analyzer/rowan): Licensed under Apache-2.0 OR MIT
* [roxmltree](https://github.com/RazrFalcon/roxmltree): Licensed under Apache-2.0 OR MIT
* [rustc-hash](https://github.com/rust-lang/rustc-hash): Licensed under Apache-2.0 OR MIT
* [rustc_version](https://github.com/djc/rustc-version-rs): Licensed under Apache-2.0 OR MIT
* [rustix](https://github.com/bytecodealliance/rustix): Licensed under Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT
* [rustversion](https://github.com/dtolnay/rustversion): Licensed under Apache-2.0 OR MIT
* [rustybuzz](https://github.com/harfbuzz/rustybuzz): Licensed under MIT
* [same-file](https://github.com/BurntSushi/same-file): Licensed under MIT OR Unlicense
* [scoped-tls-hkt](https://github.com/Diggsey/scoped-tls-hkt): Licensed under Apache-2.0 OR MIT
* [scopeguard](https://github.com/bluss/scopeguard): Licensed under Apache-2.0 OR MIT
* [semver](https://github.com/dtolnay/semver): Licensed under Apache-2.0 OR MIT
* [serde](https://github.com/serde-rs/serde): Licensed under Apache-2.0 OR MIT
* [serde_core](https://github.com/serde-rs/serde): Licensed under Apache-2.0 OR MIT
* [serde_derive](https://github.com/serde-rs/serde): Licensed under Apache-2.0 OR MIT
* [serde_json](https://github.com/serde-rs/json): Licensed under Apache-2.0 OR MIT
* [serde_repr](https://github.com/dtolnay/serde-repr): Licensed under Apache-2.0 OR MIT
* [serde_spanned](https://github.com/toml-rs/toml): Licensed under Apache-2.0 OR MIT
* [shlex](https://github.com/comex/rust-shlex): Licensed under Apache-2.0 OR MIT
* [signal-hook-registry](https://github.com/vorner/signal-hook): Licensed under Apache-2.0 OR MIT
* [simd-adler32](https://github.com/mcountryman/simd-adler32): Licensed under MIT
* [simd_helpers](https://github.com/lu-zero/simd_helpers): Licensed under MIT
* [simplecss](https://github.com/linebender/simplecss): Licensed under Apache-2.0 OR MIT
* [siphasher](https://github.com/jedisct1/rust-siphash): Licensed under Apache-2.0 OR MIT
* [slab](https://github.com/tokio-rs/slab): Licensed under MIT
* [slint](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [slint-build](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [slint-macros](https://github.com/slint-ui/slint): Licensed under GPL-3.0 OR LicenseRef-Slint-Royalty-free-2.0 OR LicenseRef-Slint-Software-3.0
* [slotmap](https://github.com/orlp/slotmap): Licensed under Zlib
* [smallvec](https://github.com/servo/rust-smallvec): Licensed under Apache-2.0 OR MIT
* [smol_str](https://github.com/rust-lang/rust-analyzer/tree/master/lib/smol_str): Licensed under Apache-2.0 OR MIT
* [softbuffer](https://github.com/rust-windowing/softbuffer): Licensed under Apache-2.0 OR MIT
* [spin_on](None): Licensed under Apache-2.0 OR MIT
* [stable_deref_trait](https://github.com/storyyeller/stable_deref_trait): Licensed under Apache-2.0 OR MIT
* [strict-num](https://github.com/RazrFalcon/strict-num): Licensed under MIT
* [strum](https://github.com/Peternator7/strum): Licensed under MIT
* [strum_macros](https://github.com/Peternator7/strum): Licensed under MIT
* [svgtypes](https://github.com/linebender/svgtypes): Licensed under Apache-2.0 OR MIT
* [syn](https://github.com/dtolnay/syn): Licensed under Apache-2.0 OR MIT
* [synstructure](https://github.com/mystor/synstructure): Licensed under MIT
* [sys-locale](https://github.com/1Password/sys-locale): Licensed under Apache-2.0 OR MIT
* [tempfile](https://github.com/Stebalien/tempfile): Licensed under Apache-2.0 OR MIT
* [termcolor](https://github.com/BurntSushi/termcolor): Licensed under MIT OR Unlicense
* [text-size](https://github.com/rust-analyzer/text-size): Licensed under Apache-2.0 OR MIT
* [thiserror](https://github.com/dtolnay/thiserror): Licensed under Apache-2.0 OR MIT
* [thiserror-impl](https://github.com/dtolnay/thiserror): Licensed under Apache-2.0 OR MIT
* [tiff](https://github.com/image-rs/image-tiff): Licensed under MIT
* [time](https://github.com/time-rs/time): Licensed under Apache-2.0 OR MIT
* [time-core](https://github.com/time-rs/time): Licensed under Apache-2.0 OR MIT
* [tiny-skia](https://github.com/RazrFalcon/tiny-skia): Licensed under BSD-3-Clause
* [tiny-skia-path](https://github.com/RazrFalcon/tiny-skia/tree/master/path): Licensed under BSD-3-Clause
* [tinystr](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [tinyvec](https://github.com/Lokathor/tinyvec): Licensed under Apache-2.0 OR MIT OR Zlib
* [tinyvec_macros](https://github.com/Soveu/tinyvec_macros): Licensed under Apache-2.0 OR MIT OR Zlib
* [toml_datetime](https://github.com/toml-rs/toml): Licensed under Apache-2.0 OR MIT
* [toml_edit](https://github.com/toml-rs/toml): Licensed under Apache-2.0 OR MIT
* [toml_parser](https://github.com/toml-rs/toml): Licensed under Apache-2.0 OR MIT
* [toml_write](https://github.com/toml-rs/toml): Licensed under Apache-2.0 OR MIT
* [tracing](https://github.com/tokio-rs/tracing): Licensed under MIT
* [tracing-attributes](https://github.com/tokio-rs/tracing): Licensed under MIT
* [tracing-core](https://github.com/tokio-rs/tracing): Licensed under MIT
* [ttf-parser](https://github.com/harfbuzz/ttf-parser): Licensed under Apache-2.0 OR MIT
* [typed-index-collections](https://github.com/zheland/typed-index-collections): Licensed under Apache-2.0 OR MIT
* [uncased](https://github.com/SergioBenitez/uncased): Licensed under Apache-2.0 OR MIT
* [unicode-bidi](https://github.com/servo/unicode-bidi): Licensed under Apache-2.0 OR MIT
* [unicode-bidi-mirroring](https://github.com/RazrFalcon/unicode-bidi-mirroring): Licensed under Apache-2.0 OR MIT
* [unicode-ccc](https://github.com/RazrFalcon/unicode-ccc): Licensed under Apache-2.0 OR MIT
* [unicode-ident](https://github.com/dtolnay/unicode-ident): Licensed under (Apache-2.0 OR MIT) AND Unicode-3.0
* [unicode-linebreak](https://github.com/axelf4/unicode-linebreak): Licensed under Apache-2.0
* [unicode-properties](https://github.com/unicode-rs/unicode-properties): Licensed under Apache-2.0 OR MIT
* [unicode-script](https://github.com/unicode-rs/unicode-script): Licensed under Apache-2.0 OR MIT
* [unicode-segmentation](https://github.com/unicode-rs/unicode-segmentation): Licensed under Apache-2.0 OR MIT
* [unicode-vo](https://github.com/RazrFalcon/unicode-vo): Licensed under Apache-2.0 OR MIT
* [unicode-xid](https://github.com/unicode-rs/unicode-xid): Licensed under Apache-2.0 OR MIT
* [unty](https://github.com/bincode-org/unty): Licensed under Apache-2.0 OR MIT
* [url](https://github.com/servo/rust-url): Licensed under Apache-2.0 OR MIT
* [usvg](https://github.com/linebender/resvg): Licensed under Apache-2.0 OR MIT
* [utf8_iter](https://github.com/hsivonen/utf8_iter): Licensed under Apache-2.0 OR MIT
* [uuid](https://github.com/uuid-rs/uuid): Licensed under Apache-2.0 OR MIT
* [v_frame](https://github.com/rust-av/v_frame): Licensed under BSD-2-Clause
* [version_check](https://github.com/SergioBenitez/version_check): Licensed under Apache-2.0 OR MIT
* [void](https://github.com/reem/rust-void.git): Licensed under MIT
* [vtable](https://github.com/slint-ui/slint): Licensed under Apache-2.0 OR MIT
* [vtable-macro](https://github.com/slint-ui/slint): Licensed under Apache-2.0 OR MIT
* [walkdir](https://github.com/BurntSushi/walkdir): Licensed under MIT OR Unlicense
* [wasm-bindgen](https://github.com/wasm-bindgen/wasm-bindgen): Licensed under Apache-2.0 OR MIT
* [wasm-bindgen-macro](https://github.com/wasm-bindgen/wasm-bindgen/tree/master/crates/macro): Licensed under Apache-2.0 OR MIT
* [wasm-bindgen-macro-support](https://github.com/wasm-bindgen/wasm-bindgen/tree/master/crates/macro-support): Licensed under Apache-2.0 OR MIT
* [wasm-bindgen-shared](https://github.com/wasm-bindgen/wasm-bindgen/tree/master/crates/shared): Licensed under Apache-2.0 OR MIT
* [weezl](https://github.com/image-rs/weezl): Licensed under Apache-2.0 OR MIT
* [which](https://github.com/harryfei/which-rs.git): Licensed under MIT
* [winit](https://github.com/rust-windowing/winit): Licensed under Apache-2.0
* [winnow](https://github.com/winnow-rs/winnow): Licensed under MIT
* [writeable](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [xkbcommon-dl](https://github.com/rust-windowing/xkbcommon-dl): Licensed under MIT
* [xkeysym](https://github.com/notgull/xkeysym): Licensed under Apache-2.0 OR MIT OR Zlib
* [xmlwriter](https://github.com/RazrFalcon/xmlwriter): Licensed under MIT
* [y4m](https://github.com/image-rs/y4m.git): Licensed under MIT
* [yoke](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [yoke-derive](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [zbus](https://github.com/z-galaxy/zbus/): Licensed under MIT
* [zbus_macros](https://github.com/z-galaxy/zbus/): Licensed under MIT
* [zbus_names](https://github.com/z-galaxy/zbus/): Licensed under MIT
* [zerocopy](https://github.com/google/zerocopy): Licensed under Apache-2.0 OR BSD-2-Clause OR MIT
* [zerocopy-derive](https://github.com/google/zerocopy): Licensed under Apache-2.0 OR BSD-2-Clause OR MIT
* [zerofrom](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [zerofrom-derive](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [zerotrie](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [zerovec](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [zerovec-derive](https://github.com/unicode-org/icu4x): Licensed under Unicode-3.0
* [zmij](https://github.com/dtolnay/zmij): Licensed under MIT
* [zune-core](https://github.com/etemesi254/zune-image): Licensed under Apache-2.0 OR MIT OR Zlib
* [zune-inflate](None): Licensed under Apache-2.0 OR MIT OR Zlib
* [zune-jpeg](https://github.com/etemesi254/zune-image/tree/dev/crates/zune-jpeg): Licensed under Apache-2.0 OR MIT OR Zlib
* [zvariant](https://github.com/z-galaxy/zbus/): Licensed under MIT
* [zvariant_derive](https://github.com/z-galaxy/zbus/): Licensed under MIT
* [zvariant_utils](https://github.com/z-galaxy/zbus/): Licensed under MIT
<!-- end cargo dependencies (handheld) -->

<!-- begin cargo dependencies (handheld-dfu) -->
* [allocator-api2](https://github.com/zakarumych/allocator-api2): Licensed under Apache-2.0 OR MIT
* [autocfg](https://github.com/cuviper/autocfg): Licensed under Apache-2.0 OR MIT
* [base64](https://github.com/marshallpierce/rust-base64): Licensed under Apache-2.0 OR MIT
* [bitfield](https://github.com/dzamlo/rust-bitfield): Licensed under Apache-2.0 OR MIT
* [bitfield-macros](https://github.com/dzamlo/rust-bitfield): Licensed under Apache-2.0 OR MIT
* [bitflags](https://github.com/bitflags/bitflags): Licensed under Apache-2.0 OR MIT
* [bitmask](https://github.com/d3lio/bitmask): Licensed under Apache-2.0 OR MIT
* [block-buffer](https://github.com/RustCrypto/utils): Licensed under Apache-2.0 OR MIT
* [bytemuck](https://github.com/Lokathor/bytemuck): Licensed under Apache-2.0 OR MIT OR Zlib
* [byteorder](https://github.com/BurntSushi/byteorder): Licensed under MIT OR Unlicense
* [cfg-if](https://github.com/rust-lang/cfg-if): Licensed under Apache-2.0 OR MIT
* [const-default](https://github.com/AerialX/const-default.rs): Licensed under MIT
* [cordyceps](https://github.com/hawkw/mycelium): Licensed under MIT
* [critical-section](https://github.com/rust-embedded/critical-section): Licensed under Apache-2.0 OR MIT
* [crypto-common](https://github.com/RustCrypto/traits): Licensed under Apache-2.0 OR MIT
* [darling](https://github.com/TedDriggs/darling): Licensed under MIT
* [darling_core](https://github.com/TedDriggs/darling): Licensed under MIT
* [darling_macro](https://github.com/TedDriggs/darling): Licensed under MIT
* [delegate](https://github.com/kobzol/rust-delegate): Licensed under Apache-2.0 OR MIT
* [digest](https://github.com/RustCrypto/traits): Licensed under Apache-2.0 OR MIT
* [document-features](https://github.com/slint-ui/document-features): Licensed under Apache-2.0 OR MIT
* [embassy-embedded-hal](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-executor](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-executor-macros](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-executor-timer-queue](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-futures](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-hal-internal](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-net-driver](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-net-driver-channel](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-sync](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-time](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-time-driver](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-time-queue-utils](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-usb](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-usb-driver](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embassy-usb-synopsys-otg](https://github.com/embassy-rs/embassy): Licensed under Apache-2.0 OR MIT
* [embedded-can](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-hal](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-hal-async](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-io](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-io-async](https://github.com/rust-embedded/embedded-hal): Licensed under Apache-2.0 OR MIT
* [embedded-storage](https://github.com/rust-embedded-community/embedded-storage): Licensed under Apache-2.0 OR MIT
* [embedded-storage-async](https://github.com/rust-embedded-community/embedded-storage): Licensed under Apache-2.0 OR MIT
* [enumset](https://github.com/Lymia/enumset): Licensed under Apache-2.0 OR MIT
* [enumset_derive](https://github.com/Lymia/enumset): Licensed under Apache-2.0 OR MIT
* [equivalent](https://github.com/indexmap-rs/equivalent): Licensed under Apache-2.0 OR MIT
* [esp-alloc](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-bootloader-esp-idf](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-config](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-hal](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-hal-procmacros](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-metadata-generated](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-println](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-radio-rtos-driver](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-rom-sys](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-rtos](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-storage](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-sync](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [esp-synopsys-usb-otg](https://github.com/esp-rs-compat/synopsys-usb-otg): Licensed under MIT
* [esp32s3](https://github.com/esp-rs/esp-pacs): Licensed under Apache-2.0 OR MIT
* [fnv](https://github.com/servo/rust-fnv): Licensed under Apache-2.0 OR MIT
* [fugit](https://github.com/korken89/fugit): Licensed under Apache-2.0 OR MIT
* [futures-core](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-sink](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-task](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [futures-util](https://github.com/rust-lang/futures-rs): Licensed under Apache-2.0 OR MIT
* [gcd](https://github.com/frewsxcv/rust-gcd): Licensed under Apache-2.0 OR MIT
* [generic-array](https://github.com/fizyk20/generic-array.git): Licensed under MIT
* [ghostfat](https://github.com/ryankurte/ghostfat): Licensed under MPL-2.0
* [hash32](https://github.com/japaric/hash32): Licensed under Apache-2.0 OR MIT
* [hashbrown](https://github.com/rust-lang/hashbrown): Licensed under Apache-2.0 OR MIT
* [heapless](https://github.com/rust-embedded/heapless): Licensed under Apache-2.0 OR MIT
* [heck](https://github.com/withoutboats/heck): Licensed under Apache-2.0 OR MIT
* [ident_case](https://github.com/TedDriggs/ident_case): Licensed under Apache-2.0 OR MIT
* [indexmap](https://github.com/indexmap-rs/indexmap): Licensed under Apache-2.0 OR MIT
* [indoc](https://github.com/dtolnay/indoc): Licensed under Apache-2.0 OR MIT
* [instability](https://github.com/ratatui/instability): Licensed under MIT
* [itm_logger](https://github.com/cs2dsb/itm_logger.rs): Licensed under Apache-2.0 OR MIT
* [itoa](https://github.com/dtolnay/itoa): Licensed under Apache-2.0 OR MIT
* [jiff](https://github.com/BurntSushi/jiff): Licensed under MIT OR Unlicense
* [libc](https://github.com/rust-lang/libc): Licensed under Apache-2.0 OR MIT
* [linked_list_allocator](https://github.com/phil-opp/linked-list-allocator): Licensed under Apache-2.0 OR MIT
* [litrs](https://github.com/LukasKalbertodt/litrs): Licensed under Apache-2.0 OR MIT
* [log](https://github.com/rust-lang/log): Licensed under Apache-2.0 OR MIT
* [memchr](https://github.com/BurntSushi/memchr): Licensed under MIT OR Unlicense
* [nb](https://github.com/rust-embedded/nb): Licensed under Apache-2.0 OR MIT
* [num-traits](https://github.com/rust-num/num-traits): Licensed under Apache-2.0 OR MIT
* [object](https://github.com/gimli-rs/object): Licensed under Apache-2.0 OR MIT
* [packing](https://github.com/cs2dsb/stm32-usb.rs): Licensed under Apache-2.0 OR MIT
* [packing_codegen](https://github.com/cs2dsb/stm32-usb.rs): Licensed under Apache-2.0 OR MIT
* [paste](https://github.com/dtolnay/paste): Licensed under Apache-2.0 OR MIT
* [pin-project-lite](https://github.com/taiki-e/pin-project-lite): Licensed under Apache-2.0 OR MIT
* [pin-utils](https://github.com/rust-lang-nursery/pin-utils): Licensed under Apache-2.0 OR MIT
* [portable-atomic](https://github.com/taiki-e/portable-atomic): Licensed under Apache-2.0 OR MIT
* [proc-macro-crate](https://github.com/bkchr/proc-macro-crate): Licensed under Apache-2.0 OR MIT
* [proc-macro2](https://github.com/dtolnay/proc-macro2): Licensed under Apache-2.0 OR MIT
* [quote](https://github.com/dtolnay/quote): Licensed under Apache-2.0 OR MIT
* [ral-registers](https://github.com/adamgreig/ral-registers): Licensed under Apache-2.0 OR MIT
* [rand_core](https://github.com/rust-random/rand_core): Licensed under Apache-2.0 OR MIT
* [rlsf](https://github.com/yvt/rlsf): Licensed under Apache-2.0 OR MIT
* [rustversion](https://github.com/dtolnay/rustversion): Licensed under Apache-2.0 OR MIT
* [ryu](https://github.com/dtolnay/ryu): Licensed under Apache-2.0 OR BSL-1.0
* [serde](https://github.com/serde-rs/serde): Licensed under Apache-2.0 OR MIT
* [serde_core](https://github.com/serde-rs/serde): Licensed under Apache-2.0 OR MIT
* [serde_derive](https://github.com/serde-rs/serde): Licensed under Apache-2.0 OR MIT
* [serde_yaml](https://github.com/dtolnay/serde-yaml): Licensed under Apache-2.0 OR MIT
* [somni-expr](https://github.com/bugadani/somni): Licensed under Apache-2.0 OR MIT
* [somni-parser](https://github.com/bugadani/somni): Licensed under Apache-2.0 OR MIT
* [stable_deref_trait](https://github.com/storyyeller/stable_deref_trait): Licensed under Apache-2.0 OR MIT
* [static_cell](https://github.com/embassy-rs/static-cell): Licensed under Apache-2.0 OR MIT
* [strsim](https://github.com/rapidfuzz/strsim-rs): Licensed under MIT
* [strum](https://github.com/Peternator7/strum): Licensed under MIT
* [strum_macros](https://github.com/Peternator7/strum): Licensed under MIT
* [svgbobdoc](https://github.com/yvt/svgbobdoc): Licensed under Apache-2.0 OR MIT
* [syn](https://github.com/dtolnay/syn): Licensed under Apache-2.0 OR MIT
* [termcolor](https://github.com/BurntSushi/termcolor): Licensed under MIT OR Unlicense
* [toml_datetime](https://github.com/toml-rs/toml): Licensed under Apache-2.0 OR MIT
* [toml_edit](https://github.com/toml-rs/toml): Licensed under Apache-2.0 OR MIT
* [toml_parser](https://github.com/toml-rs/toml): Licensed under Apache-2.0 OR MIT
* [typenum](https://github.com/paholg/typenum): Licensed under Apache-2.0 OR MIT
* [uf2_block](https://github.com/cs2dsb/stm32-usb.rs): Licensed under Apache-2.0 OR MIT
* [ufmt-write](https://github.com/japaric/ufmt): Licensed under Apache-2.0 OR MIT
* [unicode-ident](https://github.com/dtolnay/unicode-ident): Licensed under (Apache-2.0 OR MIT) AND Unicode-3.0
* [unicode-width](https://github.com/unicode-rs/unicode-width): Licensed under Apache-2.0 OR MIT
* [unsafe-libyaml](https://github.com/dtolnay/unsafe-libyaml): Licensed under MIT
* [usb-device](https://github.com/rust-embedded-community/usb-device): Licensed under MIT
* [usbd_bulk_only_transport](https://github.com/cs2dsb/stm32-usb.rs): Licensed under Apache-2.0 OR MIT
* [usbd_mass_storage](https://github.com/cs2dsb/stm32-usb.rs): Licensed under Apache-2.0 OR MIT
* [usbd_scsi](https://github.com/cs2dsb/stm32-usb.rs): Licensed under Apache-2.0 OR MIT
* [vcell](https://github.com/japaric/vcell): Licensed under Apache-2.0 OR MIT
* [version_check](https://github.com/SergioBenitez/version_check): Licensed under Apache-2.0 OR MIT
* [void](https://github.com/reem/rust-void.git): Licensed under MIT
* [winnow](https://github.com/winnow-rs/winnow): Licensed under MIT
* [xtensa-lx](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [xtensa-lx-rt](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
* [xtensa-lx-rt-proc-macros](https://github.com/esp-rs/esp-hal): Licensed under Apache-2.0 OR MIT
<!-- end cargo dependencies (handheld-dfu) -->


### Handheld Miscellaneous

* [Ark Pixel Font](https://github.com/TakWolf/ark-pixel-font/): Copyright (c) 2012, TakWolf (https://takwolf.com), licensed under the [SIL Open Font License, Version 1.1](https://github.com/TakWolf/ark-pixel-font/blob/master/LICENSE-OFL).
* [SameBoy](https://github.com/LIJI32/SameBoy/): Copyright (c) 2015-2026 Lior Halphon, licensed under the [Expat License](https://github.com/LIJI32/SameBoy/blob/master/LICENSE)
* [gba-bios](https://github.com/Cult-of-GBA/BIOS): Copyright (c) 2020-2021 DenSinH and fleroviux, licensed under the [MIT License](https://github.com/Cult-of-GBA/BIOS/blob/master/LICENSE)
* [FlashGBX LK Firmware](https://github.com/Lesserkuma/FlashGBX_LK_Firmware/): Copyright (c) Lesserkuma, licensed under the [GNU General Public License v3.0](https://github.com/Lesserkuma/FlashGBX_LK_Firmware/blob/main/LICENSE)

### Handheld Gateware

* [Chisel](https://github.com/chipsalliance/chisel): Licensed under the [Apache License 2.0](https://github.com/chipsalliance/chisel/blob/main/LICENSE)
* [scala-csv](https://github.com/tototoshi/scala-csv): Copyright (c) 2013-2015 Toshiyuki Takahashi, licensed under the [Apache License 2.0](https://github.com/tototoshi/scala-csv/blob/master/LICENSE.txt)
* [upickle](https://github.com/com-lihaoyi/upickle): Copyright (c) 2016 haoyi.sg@gmail.com, licensed under the [MIT License](https://github.com/com-lihaoyi/upickle/blob/main/LICENSE)
* [edalize](https://github.com/olofk/edalize): Copyright (c) 2018 Olof Kindgren, edalize contributors, licensed under the [BSD 2-Clause License](https://github.com/olofk/edalize/blob/main/LICENSE)
* [hdmi](https://github.com/hdl-util/hdmi): Copyright (c) 2019 Sameer Puri, licensed under the [MIT License](https://github.com/hdl-util/hdmi/blob/master/LICENSE-MIT) or [Apache License 2.0](https://github.com/hdl-util/hdmi/blob/master/LICENSE-APACHE)

### Dock Firmware

* [Raspberry Pi Pico SDK](https://github.com/raspberrypi/pico-sdk): Copyright (c) 2020 Raspberry Pi (Trading) Ltd., licensed under the [BSD 3-Clause License](https://github.com/raspberrypi/pico-sdk/blob/master/LICENSE.TXT)
* [FreeRTOS-Kernel](https://github.com/FreeRTOS/FreeRTOS-Kernel): Licensed under the [MIT License](https://github.com/FreeRTOS/FreeRTOS-Kernel/blob/main/LICENSE.md)
* [bluepad32](https://github.com/ricardoquesada/bluepad32): Copyright (c) 2019 Ricardo Quesada, licensed under the [Apache License 2.0](https://github.com/ricardoquesada/bluepad32/blob/main/LICENSE)
* [BTstack](https://github.com/bluekitchen/btstack): Copyright (c) 2009 BlueKitchen GmbH, under [a special license](https://github.com/raspberrypi/pico-sdk/blob/master/src/rp2_common/pico_btstack/LICENSE.RP) allowing commercial use with Raspberry Pi products. Note that BTstack is *not* free software.
* [tinyusb](https://github.com/hathach/tinyusb/): Copyright (c) 2012-2026 Ha Thach (tinyusb.org), licensed under the [MIT license](https://github.com/hathach/tinyusb/blob/master/LICENSE)
* [Pico-PIO-USB](https://github.com/sekigon-gonnoc/Pico-PIO-USB/): Copyright (c) 2021 sekigon-gonnoc, licensed under the [MIT License](https://github.com/sekigon-gonnoc/Pico-PIO-USB/blob/main/LICENSE)
* [tusb_xinput](https://github.com/Ryzee119/tusb_xinput/): Copyright (c) 2020 Ryan Wendland, licensed under the [MIT License](https://github.com/Ryzee119/tusb_xinput/blob/master/LICENSE)
* [Corrosion](https://github.com/corrosion-rs/corrosion): Copyright (c) 2018 Andrew Gaspar, licensed under the [MIT License](https://github.com/corrosion-rs/corrosion/blob/master/LICENSE)


<!-- begin Cargo dependencies -->

* [enum-map](https://codeberg.org/xfix/enum-map): Licensed under Apache-2.0 OR MIT
* [enum-map-derive](https://codeberg.org/xfix/enum-map): Licensed under Apache-2.0 OR MIT
* [freertos-rust](https://github.com/lobaro/FreeRTOS-rust): Licensed under MIT
* [libm](https://github.com/rust-lang/compiler-builtins): Licensed under MIT
* [log](https://github.com/rust-lang/log): Licensed under Apache-2.0 OR MIT
* [portable-atomic](https://github.com/taiki-e/portable-atomic): Licensed under Apache-2.0 OR MIT
* [proc-macro2](https://github.com/dtolnay/proc-macro2): Licensed under Apache-2.0 OR MIT
* [quote](https://github.com/dtolnay/quote): Licensed under Apache-2.0 OR MIT
* [static_cell](https://github.com/embassy-rs/static-cell): Licensed under Apache-2.0 OR MIT
* [syn](https://github.com/dtolnay/syn): Licensed under Apache-2.0 OR MIT
* [unicode-ident](https://github.com/dtolnay/unicode-ident): Licensed under (Apache-2.0 OR MIT) AND Unicode-3.0

<!-- end Cargo dependencies -->


