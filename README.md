# Remote Sensing Economic Activity
Using satellite information to remote sense marine economic activity

## Prerequisites
As NOAA favors Windows machines (apart from Onaga which is CentOS/Linux), we will assume your local machine is running Windows and server machine Linux.  The first thing to do is have ITS install Anaconda on your local machine.  We'll run code with Python3, so make sure the Anaconda distribution is for Python3.x.

### Installing TensorFlow and TensorFlow Object Detection API
Once Anaconda is installed, open up your Anaconda Prompt by searching for it in your Windows search bar.  The following sequence of commands will all be run from within Anaconda Prompt.  Installation instructions are from this [tutorial](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/training.html) so please refer to it if you have questions.

1) In your Anaconda Prompt run:
```
pip install tensorflow
```

2) Make sure you have other dependencies by running:
```
pip install pillow Cython lxml jupyter matplotlib
```

3) Install protobuf
```
conda install protobuf
```

4) Install TensorFlow Object Detection API
Navigate to the tensorflow directory (using cd and ls commands).  If your on your local machine, it will probably be found here: c:\programdata\anaconda3\lib\site-packages\tensorflow.  You can always check where printed results from installing tensorflow to see the directory where it was installed.

From within the tensorflow directory clone the model library by running:
```
git clone https://github.com/tensorflow/models.git
```

Now navigate to the research directory and compile protobuf libraries.
```
cd models/research
protoc object_detection/protos/*.proto --python_out=.
```

Install the object detection API by running these commands.
```
cp object_detection/packages/tf2/setup.py .
python -m pip install .
```

Test the object detection API by running this from within models/reseach.
```
python object_detection/builders/model_builder_tf2_test.py
```
If installation was successful you should see something like this...
```
...
----------------------------------------------------------------------
Ran 20 tests in 29.534s

OK (skipped=1)
```

### Build directory structure
Make "addons" and "workspace" directories inside the tensorflow directiory by using `mkdir dirname`.
```
TensorFlow/
├─ addons/
├─ models/
│  ├─ community/
│  ├─ official/
│  ├─ orbit/
│  ├─ research/
│  └─ ...
└─ workspace/
```

### Installing LabelImg
We will be using LabelImg to annonate jpg files to create testing and training sets. Navigate to tensorflow/addons and clone the LabelImg repo by running this command:
```
git clone https://github.com/tzutalin/labelImg.git
```
Then, navigate to addons/LabelImg and run:
```
pyrcc5 -o libs/resources.py resources.qrc
```
Test the installation by opening LabelImg by running this command from addons/LabelImg
```
python labelImg.py
```

## Working with the Husky training demo

First, clone the husky_demo folder to your TensorFlow Workspace folder on the machine you will use.
```
TensorFlow/
├─ models/
│  ├─ community/
│  ├─ official/
│  ├─ orbit/
│  ├─ research/
│  └─ ...
└─ workspace/
   └─ husky_demo/
```
## Disclaimer
This repository is a scientific product and is not official communication of the National Oceanic and Atmospheric Administration, or the United States Department of Commerce. All NOAA GitHub project code is provided on an ‘as is’ basis and the user assumes responsibility for its use. Any claims against the Department of Commerce or Department of Commerce bureaus stemming from the use of this GitHub project will be governed by all applicable Federal law. Any reference to specific commercial products, processes, or services by service mark, trademark, manufacturer, or otherwise, does not constitute or imply their endorsement, recommendation or favoring by the Department of Commerce. The Department of Commerce seal and logo, or the seal and logo of a DOC bureau, shall not be used in any manner to imply endorsement of any commercial product or activity by DOC or the United States Government.
