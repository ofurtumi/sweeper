const ul = document.querySelector("#event-list");
let listItems;

async function fetchItems () {
    listItems = await fetch('./testdata2.json');
    listItems = await listItems.json()
    console.log('listItems --> ', listItems)
    listItems = listItems.reverse()
    listItems.forEach(ev => {
        let li = document.createElement('li');
        let id = document.createElement('p');
        let tit = document.createElement('p');
        let start = document.createElement('p');
        let date = new Date(ev.start)

        tit.textContent = ev.title
        start.textContent = date.toUTCString()
        id.textContent = ev.id
        li.appendChild(id)
        li.appendChild(tit)
        li.appendChild(start)
        ul.appendChild(li)
    });
}
fetchItems()



