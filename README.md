# Taraplotlib

A cosy matplotlib styles for tea and cat lovers, inspired by the one and only [Tara Murphy](https://murphytarra.wixsite.com/tara-murphy-website), part-time science communicator and professional tea drinker.

`taraplotlib` (aka `tpl`) is a quirky little thing that tries to recreate in a plot the feeling of sipping a cup of warm tea in a rainy day.

How did we do it? Let's see some examples!

If we try to plot a line...

``` python
x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()
ax.plot(x, x)
```

![single-line](https://github.com/LorenzoPeri17/TaraPlotLib/blob/main/taraplotlib/examples/single_line.png?raw=true)

... a line of steaming hot teacups appears! And in a nice pastel color, non of that professional-looking default blue!

> Full example available in `taraplotlib/examples/single-line.py`

I wonder what happens if I try to plot multiple lines...?

![simple-plot](https://github.com/LorenzoPeri17/TaraPlotLib/blob/main/taraplotlib/examples/simple_plot.png?raw=true)
> Full example available in `taraplotlib/examples/simple_plot.py`

More pastel colors! And more nice little silhouettes!  And we haven't even mentioned the cat in the background! That's a plot carrying one heck of a cosy vibe, right?

And to the purists in the room that have noticed, yes, by default `tpl` plots (cute) _markers_, with very faint _lines_. "But what if I have too many data points? Won't the plot get too crowded?", I hear you ask. And to you - you know who you are - I reply that no! With a little [matpllotlib dark magic](https://matplotlib.org/stable/gallery/lines_bars_and_markers/markevery_demo.html) we can make sure everything stays nice and cosy even with loads of data points. However, I can't but wonder _why_ you have _so many_ data points that you think this might be an issue. This is a __cosy__ plotting library, and you are working too hard by the sounds of it! Stop producing so much data and go enjoy a cup of tea and maybe a movie!

But before you go, please don't forget to

```python
add_background(ax, 'cat')
```

or your favorite between the available images (`cat`, `teacup`, `teabag`, `pawprint`). You wouldn't want to miss on the cosy good vibes!

Ok, now imagine that you have a 2D dataset to plot. Let's see what happens...

![2d_plot](https://github.com/LorenzoPeri17/TaraPlotLib/blob/main/taraplotlib/examples/2d_plot.png?raw=true)
> Full example available in `taraplotlib/examples/2d_plot.py`

... what a cosy colormap! None of that harsh purple and yellow in `viridis`.

But... does that mean `tpl` has it's own colormaps? Yes! Here they are in their full glory!

![colormaps](https://github.com/LorenzoPeri17/TaraPlotLib/blob/main/taraplotlib/examples/colormaps.png?raw=true)
> Code available in `taraplotlib/examples/colormaps.py`

So, if you are convinced, please don't hesitate to join in the cosy fun of `tpl` with a simple

``` bash
pip install .
```
