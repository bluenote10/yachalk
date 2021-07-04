#!/usr/bin/env python

from chalk import chalk

print(f"before {chalk.black('Hello World')} after")
print(f"before {chalk.red('Hello World')} after")
print(f"before {chalk.green('Hello World')} after")
print(f"before {chalk.yellow('Hello World')} after")
print(f"before {chalk.blue('Hello World')} after")
print(f"before {chalk.magenta('Hello World')} after")
print(f"before {chalk.cyan('Hello World')} after")
print(f"before {chalk.white('Hello World')} after")

print(f"before {chalk.red.bg_black('Hello World')} after")
print(f"before {chalk.blue.bg_black.bg_red.bg_white('Hello World')} after")

print(chalk.bold(f"foo {chalk.red.dim('bar')} baz"))


print(chalk.red.bg_blue.underline("foo"))
