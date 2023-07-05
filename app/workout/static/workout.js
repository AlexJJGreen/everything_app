const add_exercise_btn = document.getElementById("add_exercise");
const exercise_list = document.getElementById("exercises");

const test_exercises = [
    "Squat", "Bench Press", "Deadlift"
]


add_exercise_btn.addEventListener("click", (e) => {
    e.preventDefault();
    let exercise_card = document.createElement("div");
    exercise_card.classList = "card";

    let card_body = document.createElement("div");
    card_body.classList = "card-body";

    let exercise_name_select = document.createElement("select");
    exercise_name_select.classList = "form-select";
    exercise_name_select.id = "exercise-name";
    exercise_name_select.innerText = "TEST";
    // Add list from db
    test_exercises.forEach(e => {
        let ex = document.createElement("option");
        ex.innerText = e;
        exercise_name_select.appendChild(ex);
    });

    // Not appending
    let create_exercise_btn = document.createElement("button");
    create_exercise_btn.innerText = "Create Exercise + ";
    create_exercise_btn.type = "button";
    exercise_name_select.appendChild(create_exercise_btn);


    card_body.appendChild(exercise_name_select);
    exercise_card.appendChild(card_body);
    exercise_list.appendChild(exercise_card);
    return true
})


/*
    < div class="card" >
        <div class="card-body">

        </div>
</div >
*/

/* <label class="input-group-text" for="inputGroupSelect01">Options</label>
  <select class="form-select" id="inputGroupSelect01">
    <option selected>Choose...</option>
    <option value="1">One</option>
    <option value="2">Two</option>
    <option value="3">Three</option>
  </select> */

