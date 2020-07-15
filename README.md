# The first FULL Nintendo Switch system menu fan translation!

![pic](https://github.com/bandithedoge/switch-pl/blob/master/assets/header.png)

[Official Discord server](https://discord.io/switchhbsh)

[new GBAtemp thread](https://gbatemp.net/threads/switch-pl-full-polish-switch-system-menu-translation.535797/)

[Want to make your own?](https://github.com/bandithedoge/switch-pl/wiki/0.-Getting-started)

### What's not translated

* eShop (obviously)
* Health and Safety Information, Important Information, etc.
* "Played for X hours", "Played X days ago", etc.
* Some error messages


### How to install

#### If you're on Atmosphere 0.10.0 or higher

* Extract the [latest](https://github.com/bandithedoge/switch-pl/releases/latest) .zip file into the root of your microSD card.

OR

* Download the latest release from the Switch Homebrew Appstore

#### If you're on Atmosphere 0.9.4 or lower

* Download the [latest](https://github.com/bandithedoge/switch-pl/releases/latest) .zip file and extract the contents of the ```/atmosphere/contents/``` directory into ```/atmosphere/titles``` on your microSD card.

#### If you're on ReiNX

* Download the [latest](https://github.com/bandithedoge/switch-pl/releases/latest) .zip file and extract the contents of the ```/atmosphere/contents/``` directory into ```/reinx/titles``` on your microSD card.

#### If you're on SXOS

* Download the [latest](https://github.com/bandithedoge/switch-pl/releases/latest) .zip file and extract the contents of the ```/atmosphere/contents/``` directory into ```/sxos/titles``` on your microSD card.
  * **NOTE: SXOS 2.5.X has broken support for LayeredFS. Use a newer version.**

### Special thanks

* Migush - for providing a full dump of the Switch system menu
* Pekempy - for his awesome [custom icon and label tutorial](https://github.com/pekempy/SwitchIconMod/wiki/Custom-Labels)
* newget - for sending his unreleased Korean translation
* Everyone who helped in the [Qcean Discord](https://discord.gg/EyxSS8T)

# Additional info

### OMG SZS!

> Sharing any .szs files is ILLEGAL!

No, it's not. Well, it depends. The .szs format is the compression format Nintendo uses. You can use it to compress anything. It can be a copyrighted Switch menu asset or a cat picture. In the case of translations, .szs files taken straight from the console contain .msbt files, which have copyrighted text. We replace the strings in the .msbt files with our own versions so they're legal to distriubute.

> But you could use patches, right?

Yes, we could, but it's not convenient at all. Patches are good for ROM hacks, where you apply a patch to an unmodified ROM. The Switch menu contains a lot of files. Dumping, extracting, patching, compressing and putting the files in the right folder would take a good few hours (unless someone bothers to write a script for it). It's just way easier to extract a .zip to a directory.

### Who is this even for?

> All Switch hacking tutorials are in English anyway, and this requires CFW. Why bother?

If you're an advanced user, you probably know English. This translation is useful if you:

* Want to give a hacked Switch to someone who doesn't know English
* Bought a hacked Switch and have no idea what to do
* Just want to mod the hell outta the console for fun
