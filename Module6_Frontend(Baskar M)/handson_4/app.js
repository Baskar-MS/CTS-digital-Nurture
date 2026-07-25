// ----------------------------
// Local Course Data
// ----------------------------

const courses = [

{
id:1,
name:"HTML",
credits:3
},

{
id:2,
name:"CSS",
credits:4
},

{
id:3,
name:"JavaScript",
credits:4
},

{
id:4,
name:"React",
credits:4
},

{
id:5,
name:"Python",
credits:3
}

];

const grid =
document.querySelector(".course-grid");

const loadingCourses =
document.querySelector("#loading-courses");

const spinner =
document.querySelector("#spinner");

const notificationList =
document.querySelector("#notification-list");

const errorMessage =
document.querySelector("#error-message");

const retryBtn =
document.querySelector("#retry-btn");


// =====================================
// Task 1
// =====================================

// Promise (.then)

function fetchUser(id){

return fetch(
`https://jsonplaceholder.typicode.com/users/${id}`
)

.then(response=>response.json())

.then(user=>{

console.log(user.name);

return user;

});

}

fetchUser(1);


// async/await

async function fetchUserAsync(id){

try{

const response=
await fetch(
`https://jsonplaceholder.typicode.com/users/${id}`
);

const user=
await response.json();

console.log(user.name);

}catch(error){

console.log(error);

}

}

fetchUserAsync(2);


// Simulated Delay

function fetchAllCourses(){

return new Promise(resolve=>{

setTimeout(()=>{

resolve(courses);

},1000);

});

}


// Render Courses

function renderCourses(courseData){

grid.innerHTML="";

courseData.forEach(course=>{

const card=
document.createElement("div");

card.className="course-card";

card.innerHTML=`

<h3>${course.name}</h3>

<p>Credits: ${course.credits}</p>

`;

grid.appendChild(card);

});

}


// Loading

loadingCourses.style.display="block";

fetchAllCourses()

.then(data=>{

loadingCourses.style.display="none";

renderCourses(data);

});


// Promise.all()

Promise.all([

fetchUser(1),

fetchUser(2)

])

.then(users=>{

console.log(

users.map(user=>user.name)

);

});


// =====================================
// Task 2
// =====================================

// Reusable Fetch Function

async function apiFetch(url){

const response=

await fetch(url);

if(!response.ok){

throw new Error(

`HTTP Error: ${response.status}`

);

}

return response.json();

}


// Load Notifications

async function loadNotifications(){

spinner.style.display="block";

notificationList.innerHTML="";

errorMessage.textContent="";

retryBtn.style.display="none";

try{

const posts=

await apiFetch(

"https://jsonplaceholder.typicode.com/posts?_limit=5"

);

spinner.style.display="none";

posts.forEach(post=>{

const card=

document.createElement("div");

card.className="notification-card";

card.innerHTML=`

<h3>${post.title}</h3>

<p>${post.body}</p>

`;

notificationList.appendChild(card);

});

}catch(error){

spinner.style.display="none";

errorMessage.textContent=

"Unable to load notifications.";

retryBtn.style.display="inline-block";

}

}

loadNotifications();


// Simulated 404

async function simulate404(){

try{

await apiFetch(

"https://jsonplaceholder.typicode.com/nonexistent"

);

}catch(error){

errorMessage.textContent=

"Something went wrong while loading data.";

retryBtn.style.display="inline-block";

}

}

simulate404();


// Retry Button

retryBtn.addEventListener(

"click",

loadNotifications

);


// =====================================
// Task 3
// =====================================

// Axios Interceptor

axios.interceptors.request.use(config=>{

console.log(

"API call started:",

config.url

);

return config;

});


// Axios Fetch Function

async function axiosFetch(url){

const response=

await axios.get(url);

return response.data;

}


// Axios Example

async function loadUserPosts(){

const posts=

await axios.get(

"https://jsonplaceholder.typicode.com/posts",

{

params:{

userId:1

},

timeout:5000

}

);

console.log(posts.data);

}

loadUserPosts();


/*

Fetch vs Axios

1. Fetch requires response.json()
   Axios parses JSON automatically.

2. Fetch requires response.ok check.
   Axios throws errors automatically.

3. Fetch is built into browsers.
   Axios is an external library.

*/