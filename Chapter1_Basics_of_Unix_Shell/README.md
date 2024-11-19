


# Exploring Files and Directory 

## ls
ls short term for listing is used to see the current files in the directory 

A more informative output can be achived using -F with ls 
```bash 
ls -F
```  
which prints the following 
![alt text](resources/1.png)
-  trailing /  means its a directory. 
- trailing * means its something runnable program. 
 
Also you can use the -a (all) to see more data information on the current directory or the directory of which you want to see. 
```bash 
ls -F -a 
ls -Fa
```
which will gives us the following result
![image](resources/2.png)


# Moving around 
cd (change directory)

```bash 
cd ..
cd ../.. 
cd -
``` 
-  cd .. can be used to move back a directory 
- cd ../.. can be used to move back twice a directory 
- cd - will help us to move to previously working directory

# Creating New files and Directories 

## mkdir 
can be used to make a directory. 

# Moving and Copying  files and directories 
mv can be used to move files or change the name of the files as well 
```bash 
mv source destination
```
cp can be used for copying the fiels 
```bash 
cp source destination
```
sometimes when there are files inside the directories we cannot just use the cp source dest , cause this will copy the content for this we have to use the -r 
```bash 
cp -r source destination
```
# Removing a directory 

```bash 
rm -rv 
rm -r -v <directory_to_delete>
rm -r -v -i <directory_to_delete>
``` 
- -v will verbose what is being deleted 
- -i can be used to do interactive delete