# Simple Todos App

**Update: I was able to debug last week's assignment. See below:**

> I wasn't able to ~`meteor run ios` from the tutorial[(step 6)](https://www.meteor.com/tutorials/react/running-on-mobile).

This was fixed by updating XCode v9.1 from the App Store.

> The Private Mode for publishing did not work either [(step 10)](https://www.meteor.com/tutorials/react/publish-and-subscribe).

In the file **_imports/ui/Task.jsx_**, line 45, replace: `showPrivateButton: React.PropTypes.bool.isRequired,` for: `showPrivateButton: PropTypes.bool.isRequired,`.

Download files [here](https://github.com/margaritayong/code-literacy/raw/master/week_08/simple-todos/simple-todos.zip).
