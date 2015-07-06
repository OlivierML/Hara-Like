# Hara-Like

These scripts enable you to use Haar-Cascade algorithm to detect some objects inside an image.

Here is how to make it work:

1) Use [Click to crop](http://www.click2crop.com/) to cut your positive and negative images. Good numbers are about 500 positives and 1000 negatives.
2) Place them in  `data/positives` and `data/negatives` in jpg.
3) Create the training set with `python prepare.py`, this will create `info.dat` 
4) Create a vec file with opencv command:

```
opencv_createsamples -info info.dat -num 131 -maxidev 40 -w 24 -h 24 -vec yourmodel.vec 
```

where num is the number of positive, w and h should be equal to the size of positives (hardcoded in `prepare.py`).

5) Train a model with opencv:

```
opencv_traincascade -data test0 -vec yourmodel.vec -bg bg.dat -numStages 15 -nsplits 2 -minhitrate 0.999 -maxfalsealarm 0.5 -numPos 200 -numNeg 900 -w 24 -h 24
```
this will create a file called `test0/cascade.xml` containing your model.

6) See the result of the model on a file using `python detect.py`.





