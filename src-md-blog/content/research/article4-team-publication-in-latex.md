Title: How to write a team publication in LaTeX and dont get mad
Date: 2015-05-29 18:00
Tags: collection, phd, research, latex, writing

![Don't get mad, get motivated and use LaTeX]({filename}../images/random/dont-get-mad-use-latex.png)

A really huge amount of people around the glob use [LaTeX](http://www.latex-project.org/) as a primary software tool (or you can say "package") for writing, formating or just maintaining their own texts. Especially, it's very popular word processing package in academia, at least at part that is related to the [STEM](http://en.wikipedia.org/wiki/STEM_fields) ( **S**cience, **T**chnology, **E**ngineering, and **M**athematics).

Usually, the scientific publications are done by some group of people, who are united under by some particular idea or just by chanse. Before starting process of writing, besides the general idea of the future publication, the structure of a publication is normally identified. The early structure of the identification helps a lot in organizing a proper writing process. The structural organization usually goes beyond the conference (or any other targeted event) driven templates and would include some details about the content itself and responsibilities of particular author.

While writing a collaborative publication, one of the pain and never ending problems is an synchronization of changes. Especially, the synchronization starts to be more painful, when the content of the paper is enhancing and more and more variants are appearing from authors. And the usage of the MS Word (despite it's really amazing and very robust and popular tool for creating texts and other types of information) adding a huge amount of overhead.

In order to write a publication I usually try to organize it in a following way:

* Separate content of the publication from it's processing part
* Make process of publication writing transparent (host and share all the publication files through the dropbox)
* Organize versioning (default feature of documents hosting services like dropbox)

The process of writing is quite simple - you need to write what you what to deliver in your publication. The tricky part, besides content, is that the LaTeX paper is ""a priori" separated into smaller parts and for each part of the paper, the responsible author is assigned. The basic publication structure can be see in this [example publication](https://github.com/vdmitriyev/pylatexmerger/tree/master/sample-paper), it consists out of following folders:

* "abstract" folder contains abstract part of the publication;
* "authors" folder contains all authors listed with accordance to the conference (or other targeted event) template
* "bibliography" folder contains a bibtex formatted file with all cited works
* "models" folder contains the images, diagrams or other graphical resources used within the publication. The root of the folder usually contains the original sources, whether the sub-folder lik "png", contain a exported version of the object in particular format.
* "build-latex-win" folder contains bat files that are able to properly compile and build pdf from TeX sources (it's also possible to use pure command line or [TeXMaker](http://www.xm1math.net/texmaker/) + installed LaTeX (e.g. [MiKTeX](http://miktex.org/))to achieve same functionality)
* The root folder of the publication contains the central LaTeX file with all 'includes' directives

And in case you followed described about approach in wiring publications, you can afterwords merge the separated TeX files into a single one using following small python script from [pylatexmerger](https://github.com/vdmitriyev/pylatexmerger) on github. Basically, script automatically merges all separated part of your TeX publication in a single TeX file.
