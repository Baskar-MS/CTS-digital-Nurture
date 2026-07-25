import { courses } from "./data.js";

// ES6 Destructuring
courses.forEach(({ name, credits }) => {
    console.log(`${name} - ${credits} credits`);
});

// map()

const formattedCourses = courses.map(
    course =>
`${course.code} — ${course.name} (${course.credits} credits)`
);

console.log(formattedCourses);

// filter()

const filteredCourses =
courses.filter(course => course.credits >= 4);

console.log("Courses with >=4 credits:",
filteredCourses.length);

// reduce()

const totalCredits =
courses.reduce(
(sum, course)=>sum + course.credits,
0
);

console.log("Total Credits:", totalCredits);

// DOM

const grid =
document.querySelector(".course-grid");

const totalCreditsText =
document.querySelector("#total-credits");

const searchInput =
document.querySelector("#search-courses");

const sortButton =
document.querySelector("#sort-btn");

const selectedCourse =
document.querySelector("#selected-course");

// Render Function

function renderCourses(courseList){

    grid.innerHTML="";

    courseList.forEach(course=>{

        const article =
        document.createElement("article");

        article.className="course-card";

        article.dataset.id=course.id;

        article.innerHTML=`

            <h3>${course.name}</h3>

            <p>${course.code}</p>

            <p>Credits : ${course.credits}</p>

        `;

        grid.appendChild(article);

    });

    const credits =
    courseList.reduce(
    (sum,c)=>sum+c.credits,
    0
    );

    totalCreditsText.textContent=
    `Total Credits : ${credits}`;

}

renderCourses(courses);

// Search

searchInput.addEventListener(
"input",
(event)=>{

const keyword =
event.target.value.toLowerCase();

const result =
courses.filter(course=>

course.name
.toLowerCase()
.includes(keyword)

);

renderCourses(result);

}
);

// Sort

sortButton.addEventListener(
"click",
()=>{

const sorted =
[...courses].sort(
(a,b)=>b.credits-a.credits
);

renderCourses(sorted);

}
);

// Event Delegation

grid.addEventListener(
"click",
(event)=>{

const card =
event.target.closest(".course-card");

if(!card) return;

const id =
Number(card.dataset.id);

const selected =
courses.find(
course=>course.id===id
);

selectedCourse.textContent=
`Selected Course:
${selected.name}
| Grade: ${selected.grade}`;

});