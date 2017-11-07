# Simple Todos App

Download files [here](https://github.com/margaritayong/code-literacy/raw/master/week_08/simple-todos/simple-todos.zip).

**Update: I was able to debug last week's assignment. See below:**

> I wasn't able to launch the *iOS Simulator* on Terminal using `meteor run ios` from the tutorial. [(Step 6)](https://www.meteor.com/tutorials/react/running-on-mobile).

1. This was fixed by updating XCode v9.1 from the App Store.


> The Private Mode for publishing did not work. [(Step 10)](https://www.meteor.com/tutorials/react/publish-and-subscribe).

2. In the file **_imports/ui/Task.jsx_**, line 45, replace: 
`showPrivateButton: React.PropTypes.bool.isRequired,` for `showPrivateButton: PropTypes.bool.isRequired,`

> The command `meteor test --driver-package practicalmeteor:mocha` did not work.

3. Try running `meteor update coffeescript` before and then re-run the command above.

<p align="center">
<img src="https://github.com/margaritayong/code-literacy/blob/master/week_08/simple-todos/images/simulator_iPhoneX.png" width="400" align="center"/>
</p>
