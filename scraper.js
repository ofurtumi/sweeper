import fetch from "node-fetch";
import 'export.xml'

let file;
async function FetchFile() {file = await fetch("./export.xml"); return file}
FetchFile()
console.log(file)
