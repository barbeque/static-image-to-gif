# What is this?
It's a project to make animated gifs out of panning or otherwise manipulating a static image programmatically.

## Current effects
 * Panning horizontally

## Future (planned) effects
 * Linear panning in any direction
 * Lissajous- or other function-based panning
 * Zooming
 * Rotation
 * Shaking

## Future (planned) features
 * Customizable settings
 * Customizable looping settings (infinite loop, single loop, forwards-backwards)
 * Palette modification (flashing via inverted palette)
 * Adding text at a given frame
 * Compression of resulting frames (reduction in colour count, lossy gif compression) resulting in smaller final animated GIF sizes

# How to use
Install instructions are similar to other Python projects:
 * Install all third party libraries using `pip install -r requirements.txt`.
 * Run `gifify.py` to turn the `resized_cat.png` image into an animated gif in `output.gif`. Change settings as appropriate (TODO: fancy user interface)

# Credits
Everything in the `vendor` directory is not mine.
 * `vendor/images2gif.py`: Almar Klein, Ant1, Marius van Voorden, under BSD license. See file for details.
