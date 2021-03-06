# boost2simple

This free, open-source tool was created to make it easier for former **BoostNote** users to switch to **SimpleNote**. 
It takes one or more _BoostNote_ collection exports (in _JSON format_, see below how to get it)
and converts them to a single, _SimpleNote_-style export zip-file 
which can then easily be imported with _SimpleNote_. 
If I have done my job right, your notes will feel as if they have been in _SimpleNote_ all along.

> **Disclaimer**  
> I am not affiliated with either _SimpleNote_ or _BoostNote_.   
> I am just a guy who was a little pissed off about the way _BoostNote_ introduced 
> its 2021 subscription policies and likes to do good deeds out of spite.

## How Is _**boost2simple**_ Helping Me Leave _BoostNote_?

* Your notes' **contents** are preserved. (This would be a horrible tool if they weren't...)
* Your **tags** are preserved.
* Original **creation** and **modification dates** are preserved.

... and there are a few limitations in _SimpleNote_ that _**boost2simple**_ even helps you overcome:

* As _BoostNote_ allows users to have **collections** and **nested folders**, 
  this tool uses the opportunities of _SimpleNote_'s tag system 
  to recreate their previous structures in an intuitive way. 

* Another _BoostNote_ feature that is missing from _SimpleNote_ are **titles** for notes 
(_SimpleNote_ just uses the first line of the note for representation in a list). 
With default settings, _**boost2simple**_ adds the original title to the beginning of each 
converted note. (This can be easily deactivated, see guide below.)  
    * As many users are composing their _BoostNote_ notes with **Markdown** formatting - 
which is also possible in _SimpleNote_ - _**boost2simple**_ will by default prefix the former title 
with ```#```  before adding it, effectively turning it into an ```h1``` heading. 
(Using no Markdown turns this behaviour off, 
as well as setting _SimpleNote_'s ```markdown``` tag to ```false``` for all converted notes.)

> **_Warning:_**  
> I have not tested any of this with the newer **BoostNote.next** and do not intend to do so. 
> *__boost2simple__* and all the info here _**might**_ work just the same in this newer app, 
> but I do not know and therefore can not make any promises.

## Requirements

* __BoostNote__'s desktop app (or a valid JSON export - **NOT JUST SINGLE FILES** - see below)
* modern _Windows_ operating system (though the Python version _might_ work under Linux too).
* being comfortable using **either**:
  - an executable file from an unknown source (= me) to get a graphical interface, or  
  - Python 3.9+   

> If you are having troubles with the exe or get some ```DLL```-related error,
it is most likely due to an old version of Windows.
Please consider updating Windows accordingly.

![Graphical User Interface](https://github.com/RWitak/boost2simple/blob/master/res/gui_screenshot.png?raw=true) ![Command Line Interface](https://github.com/RWitak/boost2simple/blob/master/res/cli_screenshot.png?raw=true)  
_Which of these two options are you more comfortable with?_

## How To Use

> If you feel unsure about the things mentioned in this guide, 
> check out the **What It All Means** section below. 
> If your questions are not answered there, feel free to contact me! 
> Just try to get your old notes out of _BoostNote_ yourself quickly 
> if you are reading this in March 2021,
> as you might otherwise lose some of those notes soon!

### Getting Your Notes Out Of _BoostNote_

To take advantage of _**boost2simple**_, you first need to export 
your _BoostNote_ collection(s) properly. To do this:
1. Open the _BoostNote_ desktop app but **DO NOT UPDATE IT!** - 
   sadly, if you haven't downloaded and synchronized the app already, 
   you might not be able to get your cloud storage files with a _free account_ anymore... (March 2021) 
2. Select your collection(s) aka "workspaces" on the left one by one 
   and click ```Settings```, then ```Space``` and ```Convert Into File System based Local Space```. 
   (This actually duplicates your "workspace" instead of converting it.)
3. Now you can export the selected "workspace" to a folder on your computer.
  The resulting export will look like this:
        
        Export folder  
        ???   boostnote.json  
        ???     
        ????????????attachments  
        ????????????notes  
4. If you are attached to your attachments, this is the time to get them out of here. 
   You won't be having them in _SimpleNote_.
5. For converting, we only need the content of ```notes```, which are JSON files holding your notes.
   If you only had a single "workspace" in _BoostNote_ 
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
        ????????????CollectionA  
        ???   ???   abc.json  
        ???   ???   efg.json  
        ???   ...  
        ???  
        ????????????CollectionB  
        ???   ???   zyx.json  
        ???   ???   wvu.json  
        ???   ...  
        ...  
   In this example, you would pick ```BoostNotes``` as import folder,
   and your automatically created new tags would be called  ```CollectionA``` and ```CollectionB```. 
   All previous **sub-folders** you had before will be added to that automatically, 
   even if you don't see them right now. **Don't add them manually!**  
   


> _BoostNote_ also lets you export/share **single notes** in different formats ??? 
> which is tedious for large collections. 
> It would work as _SimpleNote_ import with the right file type, 
> but the results would be inferior to what **_boost2simple_** can do.
> 
> I have decided to only support the above export method for now. 
> If demand is high, I might add single file conversion in the future.

### Setting Up _**boost2simple**_ 

#### The Easy Way - no install necessary!

1. Download ```boost2simple.zip``` right [here](https://github.com/RWitak/boost2simple/raw/master/boost2simple.zip).
   Your browser might (...ahem, should!) warn you about downloading weird stuff from the internet.
   Please ignore it for now and download anyway.
2. _(recommended)_ Be a responsible person and scan the downloaded zip-file for viruses.
3. Extract the archive to wherever you find its contents later.
4. _(recommended)_ Scan again for good measure.
5. Run the extracted executable file (```boost2simple.exe```), 
   the interface should pop right up. 
6. I tried to make __*boost2simple*__ self-explanatory. 
   If you're still confused, please refer to the **What It All Means** section below! 

#### The Pythonic Way

1. Get boost2simple the way you usually do, either here or via ```pip install boost2simple```. 
2. Please also do ```pip install scandir``` if you don't have it already. 
   I will include it right away in an upcoming update.
3. Run ```gui.py``` or ```cli.py``` depending on your preferred interface. 
   They have the exact same functionality.
4. If you have chosen the CLI, the extensive ```--help``` will guide you through the process.  
   Short version:
   
         cli.py [-h] [--markdown | --no-markdown] [--title | --no-title] [--from ORIGIN_DIR] [--to TARGET_DIR]
        
### Importing Your Notes With _SimpleNote_

You have successfully created an export archive that looks and works _exactly_ the way 
original _SimpleNote_ archives do! Now it's time to transfer your notes.

1. Navigate to your chosen destination folder.
2. Extract the ```notes.zip``` file to reveal the following structure:

        notes  
        ???   abc.txt  
        ???   def.txt  
        ???   ...  
        ???   zyx.txt  
        ???  
        ????????????source  
        ???   ???   notes.json      <--- the import file for SimpleNote!  
        ???  
        ????????????trash  
   > If you want, you can now make a backup of this archive (in zipped or unzipped form).  
   > This is also an interesting folder to browse through 
   > if you only need some note's contents (and nothing else) in plain text...
   > You can easily find them here by name.
3. Open _SimpleNote_ and click the menu symbol in the upper left corner 
   to go to ```Settings```, then ```Tools``` and ```Import Notes```.
4. Click ```browse``` and navigate to your freshly extracted ```notes``` folder. 
   Inside it, you go to  ```source``` and pick the ```notes.json``` file.
5. When asked to "enable Markdown on all notes", you can pick whichever option you like.
   If you activated Markdown formatting during conversion, 
   it should be enabled on all files anyway.
6. Click on ```Import```. 
7. Congratulations, you did it!

### Using Your Notes 

You can now use your old notes just like regular _SimpleNote_ notes!

To really profit from **_boost2simple_**'s tag-simulated folder structure in _SimpleNote_, 
you should turn on ```Settings -> Display -> Tags -> Sort Alphabetically```! 
Now you can navigate your files by tag in the main menu, like so:
 
       Tags  
  
       /Collection1/  
       /Collection1/SubFolder1  
       /Collection1/SubFolder2  
       /Collection1/SubFolder2/SubSubFolder  
       /Collection2/  
       /Collection3/  
       ...  
       RegularTag1  
       RegularTag2   
       ...  

Feel free to adopt that system for future notes by adding the according tags to your notes!

### What It All Means

#### File Extensions

In this guide, all **file**s have **extensions** like ```.exe```, ```.txt```, ```.json``` or ```.zip```.
If you don't see this extension, its visibility is deactivated in your file explorer.
This is fine, and you can simply ignore the file extensions in this guide!


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
> the same way this guide you are reading was styled!

#### _"include original title"_ (aka ```--title```/```--no-title```)

If this functionality is activated (as it is by default), 
each _BoostNote_'s title will serve as first line of the converted SimpleNote,
followed by a single empty line.  
This is practical, because in _SimpleNote_'s overview, 
the first line is treated like a title anyway, and you will find your notes more easily.


## Known Issues

### Selecting Desktop as directory

If you are having trouble selecting ```Desktop```, please try a different directory instead.
This is a problem with _Windows_ and the _FolderPicker_, which I have no control over.

### Files are not showing when selecting a directory

This, too, is caused by the _FolderPicker_. 
I might look into alternatives for that since it causes some quirks,
but at the moment simply rest assured that your files are there. 
It just looks for folders and nothing else, since you can only pick those anyway.

## License & Copyright

> This program is free software: you can redistribute it and/or modify
> it under the terms of the GNU General Public License as published by
> the Free Software Foundation, either version 3 of the License, or
> (at your option) any later version.
> 
> This program is distributed in the hope that it will be useful,
> but WITHOUT ANY WARRANTY; without even the implied warranty of
> MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
> GNU General Public License for more details.
> You should have received a copy of the GNU General Public License
> along with this program.  If not, see <https://www.gnu.org/licenses/>.
> 
> ---
> 
> **_boost2simple - the BoostNote->SimpleNote converter_**
> _Copyright (c) 2021, Rafael Witak._  
