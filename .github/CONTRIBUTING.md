# Contributing to Paperback Themes

First off, thanks for taking the time to contribute!

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions.

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

## Table of Contents

- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)

## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](https://github.com/Celarye/paperback-themes/blob/master/README.md).

Before you ask a question, it is best to search for existing [Issues](https://github.com/Celarye/paperback-themes/issues) or [Discussions](https://github.com/Celarye/paperback-themes/discussions) that might help you. In case you have found a suitable issue or discussion and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/Celarye/paperback-themes/issues/new/choose) or a [Discussion](https://github.com/Celarye/paperback-themes/discussions/new/choose).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (python, pip, etc), depending on what seems relevant.

We will then take care of the issue or discussion as soon as possible.

You may always contact [@celarye](https://discord.com/users/408241180405399573) through Discord as well.

## I Want To Contribute

> ### Legal Notice
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Reporting Bugs

#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://github.com/Celarye/paperback-themes/blob/master/README.md). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/Celarye/paperback-themesissues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead use the GitHub [Security Advisory tab](https://github.com/Celarye/paperback-themes/security/advisories) for sensitive bugs.

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/Celarye/paperback-themes/issues/new).
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps. Bugs without reproduction steps will not be addressed until they can be reproduced.
- If the team is able to reproduce the issue it will be left to be [implemented by someone](#your-first-code-contribution).

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Paperback Themes, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://github.com/Celarye/paperback-themes/blob/master/README.md) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/Celarye/paperback-themes/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/Celarye/paperback-themes/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. <!-- this should only be included if the project has a GUI -->
- **Explain why this enhancement would be useful** to most Paperback Themes users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

### Your First Code Contribution

**Contributing to the Theme Creator Program:**

> There also is a program starter script.

1. Fork and clone the repository
```
git clone https://github.com/<username>/paperback-themes.git
```
2. Change to the `src` directory
```
cd paperback-themes/src
```
3. Create a virtual enviroment
```
python -m venv venv

source venv/bin/activate
```
4. Install the dependencies
```
pip install -r requirements.txt
```
5. Now you can start the program
```
python main.py
```
6. You can also build it yourself (afterwards, the program can be found in the `./dist` directory)
```
pip install -U pyinstaller

# use the "--target-arch ARCH" option to specify your architecture on macOS
pyinstaller -F -n pbt main.py
```

**Contributing to themes:** Themes can be made and edited using the Theme Creator Program, grab the latest release from the GitHub [Releases page](https://github.com/Celarye/paperback-themes/releases). You might need to build the program yourself if your specific OS/architecture build is not there, check out the above step by step guide on how to do that.

### Improving The Documentation

Updates, improvements and corrections to the documentation are always welcome.

You can fork this directory and commit your changes to that, afterwards you can make a PR.

## Styleguides
### Commit Messages

Make sure that your commit messages are clear and descriptive.

## Attribution
This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!