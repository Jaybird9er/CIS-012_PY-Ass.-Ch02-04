totalSeconds = int(input("Enter the elapsed time in seconds: "))
seconds = totalSeconds % 60
minutes = int(totalSeconds / 60 % 60)
hours = int(totalSeconds / 60 / 60)
print("\n")
print("The elapsed time in seconds = ", seconds)
print("The equivalent time in hours:minutes:seconds = ", hours, ":",
      minutes, ":", seconds, sep = "")
