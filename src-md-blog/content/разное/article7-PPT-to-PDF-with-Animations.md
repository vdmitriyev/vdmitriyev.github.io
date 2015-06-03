Title: How to export MS Power Point Slides to the PDF file and keep Animations
Date: 2015-02-23 16:00
Tags: PPT, PDF, animations, export

From time to time I need to present some content in-front of the audience. And despite I'm not a bit fan of animations, they can be really helpful during the presentations. Especially, animations within the presentations are extremely helpful when the content of the slide should be delivered step-by-step.

It's not a secret that immediately after the talk, people who attended the talk, most likely will forget most of the content. One of the possible solution is to provide people with your presentation by the end of it and unusually, to be it more "interoperable" and "system independent" the format of the distribution should be PDF.

I started to search for an solution, how the MS Power Point Slides can be exported to the PDF with animations, and found following solutions:

* [PPspliT](http://www.dia.uniroma3.it/~rimondin/downloads.php) is a PowerPoint add-in that splits animation effects into different slides
* [Neil Mitchell's VBA Script for PowerPoint -> PDF (Part 1)](http://neilmitchell.blogspot.de/2007/11/creating-pdf-from-powerpoint-with.html)
* [Neil Mitchell's VBA Script for PowerPoint -> PDF (Part 2)](http://neilmitchell.blogspot.de/2007/11/powerpoint-pdf-part-2.html)

The solution with VBA script was the best for me. Here are the steps (I have an MS Office 2013 version):

* Open your Power Point presentation and navigate to the "View" panel
* Click on Macros
* Within the Macros panel type some dummy name (like "test") and click on "Create"
    - The IDE for VBA will be opened
* Within the opened IDE for VBA replace text with the code from [here](http://neilmitchell.blogspot.de/2007/11/creating-pdf-from-powerpoint-with.html) and save it
* On the "Saving Dialog" windows click yes and close IDE for VBA
* Go to your opened Power Point presentation, click on "Macros" and run "AddElements"
* Now you can notice that the all original slides were "dimmed", and new slides were added. In newly created slides, the original slides with animations are duplicated.
    - Note that even if the original elements within the Power Point presentation located in one single block are appeared one by one, after transformation to multiple slides, the block with animations will appear only one as a whole, to overcome this issues, the elements that are animated should be separated into different blocks

I hope it helped you as it helper me.
