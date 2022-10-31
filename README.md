# sdshell

SDShell right now only takes images, resizes them to 512 x 512 by finding the centered largest 
square and scaling up or down as necessary. It also renames them to a consisten name of 
"NAME (seq).jpg" where NAME is the parameter passed via --iname and <seq> is a sequence number.
 This is useful for taking a directory full of images and preparing them for learning with 
 a Dream Booth script.
 
## Running
 
```python3 sdshell.py --srcdir <dir> --traindir <dir> --iname <conceptname>```
 
## Command line options

```Usage: python3 sdshell.py [OPTIONS]

Options:
  --srcdir TEXT          Source directory for the raw, unformatted images.
  --traindir TEXT        Storage directory for the resized training images.
  --trainwidth INTEGER   Training image width, needs to be same as height.
  --trainheight INTEGER  Training image height, needs to be same as width.
  --iname TEXT           Name for the new instance that the model should be
                         trained for.
  --help                 Show this message and exit.
  ```
  
  
