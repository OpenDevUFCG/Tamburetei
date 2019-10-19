seconds = int(input());

minutes = int(seconds/60);
seconds -= minutes*60;
hours = int(minutes/60);
minutes -= hours*60;

print(repr(hours)+":"+repr(minutes)+":"+repr(seconds))
