# April Tag Detector

This repo contains a basic application that shows you how to detect april tags using the `AprilTagDetector` in edgeIQ.

## Resources

* Pre-generated april tags and be found [here](https://github.com/AprilRobotics/apriltag-imgs).
* New april tags can be generated using this [repo](https://github.com/AprilRobotics/apriltag-generation).

## Setup

This application requires an alwaysAI account. Head to the [Sign up page](https://www.alwaysai.co/dashboard) if you don't have an account yet. Follow the instructions to install the alwaysAI tools on your development machine.

Next, create an empty project to be used with this app. When you clone this repo, you can run `aai app configure` within the repo directory and your new project will appear in the list.

## Usage

Once the alwaysAI tools are installed on your development machine (or edge device if developing directly on it) you can run the following CLI commands:

To set up the target device & install path

```
aai app configure
```

To install the app to your target (make sure you use the aai app models add command to add the current TensorRT model)

```
aai app install
```

To start the app

```
aai app start
```
