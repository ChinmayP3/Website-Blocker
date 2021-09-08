# Website-blocker-application
A python application that restricts entry into websites during some part of day.

Libraries used in this application are time and datetime for getting the current time of the day and also to give a delay in responding.
The coding part is very simple.

We first decide a duration in which we want to block the websites. We also decide which websites have to be blocked.
The we check if our current time is in the duration.
If it is then we write to the hosts file local machine ip address and the website(domain) name.
If it is outside the duration then we erase the file contents.

For more in depth understand please watch the video:
https://youtu.be/onHm4Lj5p0Y

Initial this was the code i wrote in the video as well

Link to the code written in the video:
https://drive.google.com/file/d/1JXgo9q8h_epUEIBi5UV2jQypihU4HJuK/view?usp=sharing

Later change made was that i decided to just truncate the file if it is not needed to be used.
    
    
