#!/usr/bin/env python3

import sys
import os.path
import glob
import re

if len(sys.argv) != 5:
    print("Usage: " + sys.argv[0] + " <datadir> <template> <date> <output>")
    sys.exit(1)

template_file=sys.argv[2]
date=sys.argv[3]
output=sys.argv[4].strip("./")

if not os.path.isdir(output):
    os.mkdir(output)

if  os.path.isdir(sys.argv[1]):
    dataDir=sys.argv[1]
    filenames=glob.glob(dataDir+"/*.crs") 
    
for filename in filenames:
     course=filename.strip("./data/").strip(".crs")
     if(len(course) == 7):
         course_num=re.sub(r"[A-Z]{3}", "",course)
     if(len(course) == 6):
         course_num=re.sub(r"[A-Z]{2}", "", course)
     with open(filename, "r") as infile:
         [dept_code, dept_name]=infile.readline().strip().split(maxsplit=1)
         course_name=infile.readline()
         [course_sched, course_start, course_end]=infile.readline().strip().split(maxsplit=3)
         credit_hours=infile.readline()
         num_students=infile.readline()
         if (int(num_students) > 30):
             num_students=str(num_students)
             output=sys.argv[4]+"/"+course+".warn"
             with open(template_file, "r") as templfile, open(output, "w") as out:
                 for line in templfile:
                     line=line.replace("[[dept_code]]", dept_code).replace( "[[course_num]]", course_num).replace( "[[date]]",date)
                     line=line.replace("[[course_name]]", course_name).replace("[[course_start]]",  course_start)
                     line=line.replace("[[course_end]]", course_end)
                     line=line.replace("[[num_students]]", num_students)
                     line=line.replace("[[dept_name]]", dept_name)
                     out.write(line)
                 output=""
                 out.close()
                 templfile.close()


