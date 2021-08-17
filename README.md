<h1 align="center">
	<br>
	<br>
	<img width="320" src="https://raw.githubusercontent.com/bluenote10/yachalk/master/media/logo.png" alt="Chalk">
	<br>
	<br>
	<br>
</h1>

> Terminal string styling done right

This is a feature-complete clone of the awesome [Chalk](https://github.com/chalk/chalk) (JavaScript) library.

All **credits go to [Sindre Sorhus](https://github.com/sindresorhus)**.

[![PyPI version](https://badge.fury.io/py/yachalk.svg)](https://badge.fury.io/py/yachalk)
[![Build Status](https://github.com/bluenote10/yachalk/workflows/ci/badge.svg)](https://github.com/bluenote10/yachalk/actions?query=workflow%3Aci)
[![codecov](https://codecov.io/gh/bluenote10/yachalk/branch/master/graph/badge.svg?token=6I98R2661Z)](https://codecov.io/gh/bluenote10/yachalk)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy](https://img.shields.io/badge/mypy-strict-blue)](http://mypy-lang.org/)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)


<img src="https://raw.githubusercontent.com/bluenote10/yachalk/master/media/demo1.svg" width="900">

<br>

---

<br>

## Highlights

- Fluent, auto-complete-friendly API for maximum coding efficiency
- Ability to nest styles
- Proper handling of styling edge cases (same test cases as Chalk)
- Auto-detection of terminal color capabilities
- [256/Truecolor color support](#256-and-truecolor-color-support), with fallback to basic colors depending on capabilities
- Same conventions as Chalk to manually control color modes via `FORCE_COLOR`
- No dependencies
- Fully typed (mypy strict), no stubs required


## Install

```console
$ pip install yachalk
```

The only requirement is a modern Python (3.6+).

## Usage

```python
from yachalk import chalk

print(chalk.blue("Hello world!"))
```

Chalk comes with an easy to use composable API where you just chain and nest the styles you want.

```python
from yachalk import chalk

# Combine styled and normal strings
print(chalk.blue("Hello") + " World" + chalk.red("!"))

# Compose multiple styles using the chainable API
print(chalk.blue.bg_red.bold("Hello world!"))

# Use within f-strings
print(f"Found {chalk.bold(num_results)} results.")

# Pass in multiple arguments
print(chalk.blue("Hello", "World!"))

# Nest styles...
print(chalk.red(f"Hello {chalk.underline.bg_blue('world')}!"))

# Nest styles of the same type even (color, underline, background)
print(chalk.green(
    "I am a green line " +
    chalk.blue.underline.bold("with a blue substring") +
    " that becomes green again!"
))

# Use RGB or HEX colors
print(chalk.rgb(123, 45, 67).underline("Underlined reddish color"))
print(chalk.hex("#DEADED").bold("Bold gray!"))
```

Easily define and re-use your own themes:

```python
from yachalk import chalk

error = chalk.bold.red
warning = chalk.hex("#FFA500")

print(error("Error!"))
print(warning("Warning!"))
```


## Prior art: Why yet another chalk clone?

The Python ecosystem has a large number libraries for terminal styling/coloring. However, after working with Chalk in JavaScript for a while, I always missed to have the same convenience in Python. Inspired by Chalk, I wanted to have a terminal styling library satisfying the following design criteria:

- **Automatic reset handling**: Many Python libraries require manual handling of ANSI reset codes. This is error prone, and a common source of coloring issues. It also means that these libraries cannot handle advanced edge cases like proper handling of newlines in all contexts, because that requires internal reset handling.
- **Single symbol import**: Some libraries require to import special symbols for foreground/background/modifiers/... depending on the desired styling. This is tedious in my opinion, because you have to adapt the imports all the time when you change the particular styling.
- **Auto-complete friendly**: I don't want to memorize a style/color API, I'd like to have full auto-complete support. Some existing Chalk clones seem to generate all style properties dynamically, which means that an IDE cannot support with auto-completion.
- **Support of nested styles**: Sometimes it is convenient to embed a style into an existing styled context. With Chalk this simply works. None of the libraries I tried have support of nested styles.
- **Support of edge cases**: Chalk has solutions for many edge cases like newline handling, or certain challenges in nested styles. The Python libraries I tried didn't support these. Yachalk is tested against the same test cases as Chalk, so it should support them all.
- **Not print focused**: Some libraries provide an API with a focus on offering modified `print` functions. I prefer the single responsibility principle: Styling should only do styling, and return a string. This still leaves the possibility to print the string, write it to a file, or pass it around freely.
- **True color support**: Today most terminal have true color support, so it makes sense to support it in the API. Many older Python libraries only support the basic 16 colors.
- **Capabilities auto detection / fallbacks**: Chalk is fully backwards compatible on dumber terminals, by approximating colors with what is available on a particular terminal. I haven't found this feature in existing Python libraries.
- **Zero dependencies**: Some libraries are based e.g. based on curses, which is a heavy dependency for something as simple as styling/coloring.
- **Fully typed**: I like optional typing, but often library type stubs come with bad types. Yachalk runs in strict mypy mode, which means that no stubs are needed and its type should be correct by design.

I started collecting existing libraries in a feature matrix, but since I keep finding more and more libraries, I've given up on filling it completely 😉. Nonetheless, feel free to open an issue if it contains an error or misses an important solution.

![comparison](https://raw.githubusercontent.com/bluenote10/yachalk/master/media/comparison.png)

Links to related projects:
- [termcolor](https://pypi.org/project/termcolor/)
- [colored](https://gitlab.com/dslackw/colored)
- [ansicolors](https://pypi.org/project/ansicolors/)
- [sty](https://github.com/feluxe/sty)
- [blessings](https://github.com/erikrose/blessings)
- [rich](https://github.com/willmcgugan/rich)
- [style (clr)](https://github.com/lmittmann/style)
- [pychalk](https://github.com/anthonyalmarza/chalk)
- [simple_chalk](https://pypi.org/project/simple-chalk/)


## API

In general there is no need to remember the API, because it is written in a way that it fully auto-completes in common IDEs:

![auto_complete](https://raw.githubusercontent.com/bluenote10/yachalk/master/media/auto_complete.gif)

**`chalk.<style>[.<style>...](string, [string...], sep=" ")`**

Example: `chalk.red.bold.underline("Hello", "world")`

Chain [styles](#styles) and call the last one as a method with a string argument. Order doesn't matter, and later styles take precedent in case of a conflict. This simply means that `chalk.red.yellow.green` is equivalent to `chalk.green`.

Multiple arguments will be separated by a space, but the separator can also be passed in as keyword argument `sep="..."`.


**`chalk.set_color_mode(mode: ColorMode)`**

Set the color mode manually. `ColorMode` is an enum with the value:

- `ColorMode.AllOff`
- `ColorMode.Basic16` (basic 16-color ANSI colors)
- `ColorMode.Extended256` (256-color ANSI color mode)
- `ColorMode.FullTrueColor` (full true color support)

See [color mode control](#color-mode-control) for more details.

**`chalk.disable_all_ansi()`**

Shorthand for `chalk.set_color_mode(ColorMode.AllOff)`.

**`chalk.enable_basic_colors()`**

Shorthand for `chalk.set_color_mode(ColorMode.Basic16)`.

**`chalk.enable_extended_colors()`**

Shorthand for `chalk.set_color_mode(ColorMode.Extended256)`.

**`chalk.enable_full_colors()`**

Shorthand for `chalk.set_color_mode(ColorMode.FullTrueColor)`.

**`chalk.get_color_mode() -> ColorMode`**

Return current color mode.


## Styles

### Modifiers

- `reset` - Resets the current color chain.
- `bold` - Make text bold.
- `dim` - Emitting only a small amount of light.
- `italic` - Make text italic. *(Not widely supported)*
- `underline` - Make text underline. *(Not widely supported)*
- `inverse`- Inverse background and foreground colors.
- `hidden` - Prints the text, but makes it invisible.
- `strikethrough` - Puts a horizontal line through the center of the text. *(Not widely supported)*
- `visible`- Prints the text only when Chalk has a color level > 0. Can be useful for things that are purely cosmetic.

### Colors

- `black`
- `red`
- `green`
- `yellow`
- `blue`
- `magenta`
- `cyan`
- `white`
- `black_bright` (alias: `gray`, `grey`)
- `red_bright`
- `green_bright`
- `yellow_bright`
- `blue_bright`
- `magenta_bright`
- `cyan_bright`
- `white_bright`

### Background colors

- `bg_black`
- `bg_red`
- `bg_green`
- `bg_yellow`
- `bg_blue`
- `bg_magenta`
- `bg_cyan`
- `bg_white`
- `bg_black_bright` (alias: `bg_gray`, `bg_grey`)
- `bg_red_bright`
- `bg_green_bright`
- `bg_yellow_bright`
- `bg_blue_bright`
- `bg_magenta_bright`
- `bg_cyan_bright`
- `bg_white_bright`


## 256 and Truecolor color support

Chalk supports 256 colors and [Truecolor](https://gist.github.com/XVilka/8346728) (16 million colors) on supported terminal apps.

Colors are downsampled from 16 million RGB values to an ANSI color format that is supported by the terminal emulator (or by setting a specific `ColorMode` manually). For example, Chalk configured to run at level `ColorMode.Basic16` will downsample an RGB value of #FF0000 (red) to 31 (ANSI escape for red).

Examples:

- `chalk.rgb(15, 100, 204)("Hello!")`
- `chalk.hex("#DEADED").underline("Hello, world!")`

Background versions of these models are prefixed with `bg_`:

- `chalk.bg_rgb(15, 100, 204)("Hello!")`
- `chalk.bg_hex("#DEADED").underline("Hello, world!")`


## Color mode control

The imported symbol `chalk` is a singleton that is initialized with the color mode resulting from the auto-detection. This means that if you run on a terminal that has e.g. only basic 16 colors support, you can still use the full RGB/HEX API, but the resulting colors would be approximated by the available colors. If the terminal doesn't support any ANSI escape codes, the resulting strings would be completely free of any ANSI codes.

If you would like to take manual control of the color mode, you have three options.

**1. Use environment variables**

Chalk has introduced the convention to use the `FORCE_COLOR` environment variable as an override in the auto-detection. The semantics are:

- `FORCE_COLOR=0` enforces `ColorMode.AllOff`.
- `FORCE_COLOR=1` enforces `ColorMode.Basic16`.
- `FORCE_COLOR=2` enforces `ColorMode.Extended256`.
- `FORCE_COLOR=3` enforces `ColorMode.FullTrueColor`.

This can be a convenient solution in CI/cloud-based contexts.


**2. Set the color mode manually on the `chalk` instance**

If you don't care about auto-detection, you might as well set your desired color mode unconditionally.

The `chalk` singleton supports setting the color mode via `chalk.disable_all_ansi`, `chalk.enable_..._colors`, or `chalk.set_color_mode`.

A reasonable place to configure the singleton is e.g. at the beginning of a `main` function, similar to where logging is configured.


**3. Use your own `chalk` instance**

For advanced use cases that e.g. require to dynamically switch the color mode in a multi-threaded context, you can opt-out of the convenience of using a singleton, and use a custom `chalk` instances where desired. In general `chalk` is just an instance of `ChalkFactory`, which takes the color mode as input in its constructor.


```python
from yachalk import ChalkFactory

def some_function():
    # create your own chalk instance with explicit mode control
    chalk = ChalkFactory(ColorMode.FullTrueColor)

    # ...

    colored_messages.append(chalk.red("An error occurred"))
```

Or if you'd like to use your own mode-detection logic, you could create the `chalk` singleton yourself in one of your modules

```python
# e.g. in my_chalk.py
from yachalk import ChalkFactory

def custom_color_mode_detection() -> ColorMode:
    # ...
    return ColorMode.Basic16

chalk = ChalkFactory(custom_color_mode_detection())
```

and replace usages of `from yachalk import chalk` with `from my_chalk import chalk`.
