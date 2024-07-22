# BugReportCrawler

### Bug URL Setting
Set bug report urls in <ins>bug_item_file.txt</ins>.
```sh
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=1
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=2
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=3
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=4
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=5
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=6
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=7
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=8
https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=9
```

### Usage
Run the command to download bug data (<ins>linux</ins> is the project name).
```sh
python3 main.py linux
```


### Bug XML URL Prefix Reference
<ins>Eclipse</ins>: ```https://bugs.eclipse.org/bugs/show_bug.cgi?ctype=xml&id=```   

<ins>Freedesktop</ins>: ```https://bugs.freedesktop.org/show_bug.cgi?ctype=xml&id=```  

<ins>GCC</ins>: ```https://gcc.gnu.org/bugzilla/show_bug.cgi?ctype=xml&id=```  

<ins>GNOME</ins>: ```https://bugzilla.gnome.org/show_bug.cgi?ctype=xml&id=```

<ins>KDE</ins>: ```https://bugs.kde.org/show_bug.cgi?ctype=xml&id=```  

<ins>LibreOffice</ins>: ```https://bugs.documentfoundation.org/show_bug.cgi?ctype=xml&id=```  

<ins>Linux kernel</ins>: ```https://bugzilla.kernel.org/show_bug.cgi?ctype=xml&id=```  

<ins>LLVM</ins>: ```https://bugs.llvm.org/show_bug.cgi?ctype=xml&id=```   

<ins>OpenOffice</ins>: ```https://bz.apache.org/ooo/show_bug.cgi?ctype=xml&id=```  

# Citation
You are kindly asked to acknowledge the usage of the dataset by citing the following publication:
```
@inproceedings{xiao2020hindbr,
  title={HINDBR: Heterogeneous Information Network Based Duplicate Bug Report Prediction},
  author={Xiao, Guanping and Du, Xiaoting and Sui, Yulei and Yue, Tao},
  booktitle={2020 IEEE 31st International Symposium on Software Reliability Engineering (ISSRE)},
  pages={195--206},
  year={2020},
  organization={IEEE}
}
```
