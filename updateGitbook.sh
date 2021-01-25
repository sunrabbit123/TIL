cd D:\TIL-private/docs

gitbook install && gitbook build

cp -R _book/* .

git clean -fx node_modules
git clean -fx _book

cd ..

git add .

git commit -a -m "Update github pages"

git push origin main

