# Regex 3 Notes

Find `&`

Replace with `&amp;`

Find `<` 

Replace with Nothing (no string found)

Find `>`

Replace with Nothing (no string found)
Find `\n\n{2,}`

Replace with `\n\n

Find `^.+?$`

Replace with `<p>\0</p>`

Find `.+`

Replace with `<xml>\0</xml>`

Find `<p>\s*(CHAPTER.+?)</p>`

Replace with `<heading>\1</heading>`

Find `<heading>.+?<heading>`

Replace with 
`</chapter>
<chapter>\0'

Find `"(.+?)"`

Replace with `<q>\1</q>`





