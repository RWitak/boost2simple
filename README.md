# boost2simple

This tool was created to make it easier for former **BoostNote** users to switch to **SimpleNote**. 
It takes one or more _BoostNote_ collection exports (in _JSON format_, see below how to get it)
and converts them to a single, _SimpleNote_-style export zip-file 
which can then easily be imported with _SimpleNote_. 
If I have done my job right, your notes will feel as if they have been in _SimpleNote_ all along.

> **_Warning:_**  
> I have not tested any of this with the newer **BoostNote.next** and do not intend to do so. 
> *__boost2simple__* and all the info here _**might**_ work just the same in this newer app, 
> but I do not know and therefore can not make any promises. 

## How Is _**boost2simple**_ Helping Me Leave _BoostNote_? 

* Your notes' contents are preserved. (This would be a horrible tool if they weren't...)
* Your tags are preserved.
* Creation and modification dates are preserved.

... and there are a few limitations in _SimpleNote_ that _**boost2simple**_ even helps you overcome:

* As _BoostNote_ allows users to have collections and nested folders, 
_**boost2simple**_ uses the opportunities of _SimpleNote_'s tag system 
to recreate their previous structures in an intuitive way.

* Another _BoostNote_ feature that is missing from _SimpleNote_ are titles for notes 
(_SimpleNote_ just uses the first line of the note for representation in a list). 
With default settings, _**boost2simple**_ adds the original title to the beginning of each 
converted note. (This can be easily deactivated with the ```--no-title``` flag.)  
    * As many users are composing their _BoostNote_ notes with _Markdown_ formatting - 
which is also possible in _SimpleNote_ - _**boost2simple**_ will by default prefix the former title 
with ```#```  before adding it, effectively turning it into an ```h1``` heading. 
(Using ```--no-markdown``` turns this behaviour off, 
as well as setting _SimpleNote_'s ```markdown``` tag to ```false``` for all converted notes.)

## Requirements

* Windows 10
* Python 3.9+
* __BoostNote__'s desktop app (or a valid JSON export - **!!!NOT JUST SINGLE FILES!!!** see below)
* being comfortable with a very simple command line tool 

## How To Use

### Getting Your Notes Out Of _BoostNote_

To take advantage of _**boost2simple**_, you first need to export 
your _BoostNote_ collection(s) properly. To do this:
1. Open the _BoostNote_ desktop app but **DO NOT UPDATE IT!** - 
   sadly, if you haven't downloaded and synchronized the app already, 
   you might not be able to get your cloud storage files with a free account anymore... 
2. Select your collection(s) aka "workspaces" on the left one by one 
   and click ```Settings```, then ```Space``` and ```Convert Into File System based Local Space```. 
   (This actually duplicates your "workspace" instead of converting it.)
3. Now you can export the selected "workspace" to a folder on your computer.

> _BoostNote_ also lets you export/share **single notes** in different formats, 
> which is tedious for large collections. 
> That is why I have decided to only support the above export methodology for now, 
> which saves a lot of time, but produces different file types. 
> If demand is high, I might add single file conversion in the future.

### Setting Up _**boost2simple**_ 

1. Download
