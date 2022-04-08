let searchButton = document.querySelector("#search")

//Add an event listener to the button that runs the function sendApiRequest when it is clicked
searchButton.addEventListener("click",()=>{
  console.log("button pressed")
  sendApiRequest()
})

//An asynchronous function to fetch data from the API.
async function sendApiRequest() {
  let APP_ID = "2dcffed5"
  let API_KEY = "97a6b671dd812cb4b3774a5349883579"
  let response = await fetch('https://api.edamam.com/api/recipes/v2/0123456789abcdef0123456789abcdef?app_id=YOUR_APP_ID&app_key=YOUR_APP_KEY&type=public\n');
  console.log(response)
  let data = await response.json()
  console.log(data)
  useApiData(data)
}

//function that does something with the data received from the API. The name of the function should be customized to whatever you are doing with the data
function useApiData(data){
  document.querySelector("#content").innerHTML =
      <div class="card" style="width: 18rem;">
        <img src="${data.hits[0].recipe.image}" class="card-img-top" alt"..."></img>
        <div class="card-body"/>
          <h5 class="card-title">${data.hits{0} recipe.label}</h5>
          <p class="card-test"> Something to build up the bulk for now</p>
          <a href="${data.hits[0].recipe.url}" class="btn btn-primary"> Go somewhere</a>
      </div>
®}
