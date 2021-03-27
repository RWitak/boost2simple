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

* __BoostNote__'s desktop app (or a valid JSON export - **!!!NOT JUST SINGLE FILES!!!** see below)
* modern Windows OS (though this _might_ work under Linux too)
* being comfortable using **either**:
  - an executable file from an unknown source (= me) to get a graphical interface, or
  - Python 3.9+ 

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
  The resulting export will look like this:
        
        Export folder
        │   boostnote.json
        │   
        ├───attachments
        └───notes
4. If you are attached to your attachments, this is the time to get them out of here. 
   You won't be having them in _SimpleNote_.
5. For converting, we only need the content of ```notes```, which are JSON files holding your notes.
   If you only have a single "workspace" in _BoostNote_ 
   (or don't want to get an identifying tag for your workspace),
   just pick the ```notes``` folder as import folder in _**boost2simple**_.  
   You are done here!
   
---
   
6. If you do like a little more order in your life, 
   you should rename ```notes``` to whatever you want that collection to be called from now on. 
7. Repeat the process for all workspaces.
8. Put the renamed folders into a new folder somewhere. 
   If you were to call that folder ```BoostNotes``` (for sentimental reasons), 
   the structure we are striving for would look something like this:

        BoostNotes
        ├───CollectionA
        │   │   abc.json
        │   │   efg.json
        │   │   ...
        │
        └───CollectionB
            │   zyx.json
            │   wvu.json
            │   ...
   In this example, you would pick ```BoostNotes``` as import folder,
   and your automatically created new tags would be called  ```CollectionA``` and ```CollectionB```. 
   Every previous sub-folders you had before are added to that automatically, 
   even if you don't see them right now! 
   


> _BoostNote_ also lets you export/share **single notes** in different formats ─ 
> which is tedious for large collections. 
> That is why I have decided to only support the above export method for now, 
> which saves a lot of time, but produces different file types 
> and is therefore not compatible with this tool.   
> If demand is high, I might add single file conversion in the future.

### Setting Up _**boost2simple**_ 

#### The Easy Way

1. Download ```boost2simple.exe``` right here.
2. Run it.

#### The Pythonic Way

1. Get boost2simple the way you usually do, either here or via ```pip install```.
2. Run ```gui.py``` or ```cli.py``` depending on your preferred interface. 
   They have the exact same functionality.
3. If you have chosen the CLI, the extensive ```--help``` will guide you through the process.
        
### What It All Means

#### _"use Markdown"_ (aka ```--markdown```/```--no-markdown```)

If this functionality is activated (as it is by default),
_SimpleNote_ will recognize the imported notes as _Markdown_-formatted and display them accordingly.  
Additionally, if you include the original title (see below), 
the latter will be prefixed with ```# ``` to turn it into an ```h1```-header. 
Most _SimpleNote_ clients don't display this symbol in the overview 
(the Android version does, but I hope to change that soon).
> If you didn't use _Markdown_ or don't even know what it is, 
> there is no harm in leaving this on (apart from the extra symbol), 
> but you also don't profit from it.  
> Personally, I encourage you to learn about _Markdown_, 
> because it is a great way to style plain text almost effortlessly - 
> just like this text right here!



#### _"include original title"_ (aka ```--title```/```--no-title```)

If this functionality is activated (as it is by default), 
each _BoostNote_'s title will serve as first line of the converted SimpleNote,
followed by a single empty line.  
This is practical, because in _SimpleNote_'s overview, 
the first line is treated like a title anyway and you will find your notes more easily.


## Known Issues

### Selecting Desktop as directory

If you are having trouble selecting Desktop, please try a different directory instead.
This is a problem with Windows and the FolderPicker, which I have no control over.

### My files are not showing when selecting a directory

This, too, is caused by the FolderPicker. I might look into alternatives for that since it causes some quirks,
but at the moment simply rest assured that your files are there. 
It just looks for folders and nothing else, since you can only pick those anyway.
