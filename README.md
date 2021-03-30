# SPM450
Theater Project for CSE453

**DO NOT PUSH UNSTABLE CODE HERE**

*QUICK NOTE*
 
Hardware functionality may be commented out, so that people can work on code from their desktops
 
I attempted to comment things out in a way that makes it easy to restore full functionality on RasPi

 For example

 savePro = Button(profilePage, text='Save')#, command=(lambda e=ents: sf.fetch(e)))

 This button has a # after the final parenthesis, so that i could test button without working function

 It can be restored by deleting the extra parenthesis and '#', as rest of line was preserved
