const body = document.querySelector("body");

const homeAdd = function (arg) {
    arg.classList.add("home-body");
}

//axios requests that reach our server to run SA on said story and show result inside button
const saButtons = document.querySelectorAll(".sa-button");
for (let button of saButtons) {
    button.addEventListener("click", async function (evt) {
        evt.preventDefault();
        const text = button.firstChild;
        const input = text.nextSibling;
        const value = input.value;
        const storyID = button.getAttribute('data-story')
        if (value === "Get Polarity") {
            try {
                const req = await axios.post(`/story/${storyID}/polarity`);
                const resp = req.data.response;
                input.value = resp;
            } catch (error) {
                console.error(error.response.data)
            }
        }
        else if (value === "Get Subjectivity") {
            const req = await axios.post(`/story/${storyID}/subjectivity`);
            const resp = req.data.response;
            input.value = resp;
        }
    })
}

const deleteQueryButtons = document.querySelectorAll(".close")
for (let button of deleteQueryButtons) {
    button.addEventListener("click", async function (evt) {
        console.log("CLICKEDDDD")
        const queryID = button.getAttribute('data-query')
        console.log(queryID)
        const req = await axios.post(`/user/${queryID}/delete`);
        const resp = req.data.response;
        button.value = resp;
    })
}


//Replace broken images with default image

const default_avatar = 'https://secure.gravatar.com/avatar?d=wavatar';

window.addEventListener("load", event => {
    let images = document.querySelectorAll('img');
    for (let image of images) {
        let isLoaded = image.complete && image.naturalHeight !== 0;
        if (!isLoaded) {
            image.src = default_avatar;
        }
    }
});
// Source: https://www.techiedelight.com/replace-broken-images-with-javascript/