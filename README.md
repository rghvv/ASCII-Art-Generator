# ASCII-Art-Generator
A Python script that converts images to ASCII art. Works pretty well when using cutout vector images (like logos) as input, but not so much when using real images (like one you'd take on your camera).

<h3>Requirements</h3>

* NumPy

* Pillow

* Colorama (for colored terminal text)

<h3>Usage</h3>

<code>python Ascii-Converter.py --f <infile.png> --o <outfile> --r <width> --s <scale></code>

<h4>Parameters</h4>

* <code><b>--f</b></code>: Input image filename (jpg/png/svg/etc.)

* <code><b>--o</b></code>: Output filename (.txt format is implied). Defaults to <b>ascii.txt</b>.

* <code><b>--r</b></code>: Resolution, or width of the ASCII canvas in characters, in integers. Defaults to <b>100</b>.

* <code><b>--s</b></code>: Scale, or width/height of ASCII canvas, in float. Defaults to <b>0.43</b> because it's a good value for the Courier font.

<h3>Samples</h3>

<code>python Ascii-Converter.py --f che.png --o che</code>

![Che Guevara](https://raw.githubusercontent.com/raghavverma2/ASCII-Art-Generator/master/output/cheout.png)

<code>python Ascii-Converter.py --f fire.png --o fire</code>

![Fire](https://raw.githubusercontent.com/raghavverma2/ASCII-Art-Generator/master/output/fireout.png)

<code>python Ascii-Converter.py --f wave.png --o wave --r 235</code>

![Wave of Kanagawa](https://raw.githubusercontent.com/raghavverma2/ASCII-Art-Generator/master/output/waveout.png)
