
Sprites
=======

Now that we have our image bank the next step is to actually get some images showing up on the screen. The first thing we will do is fill the background with the first (or zeroith, if you are a computer scientist) image in our image bank. We will take the image and just place it over and over again tiling it all over the screen. Since the image is just a plain white square, this will just make the entire background white for us.

Luckaly CircuitPython has some built in libraries that will make this much easier for use. We will be using 2, :file:`ugame` and :file:`stage`. We will import these 2 libraries and then we will write the following code:

.. literalinclude:: ./code/code.py
   :language: python
   :caption: code.py
   :linenos: 1-29, 38-


