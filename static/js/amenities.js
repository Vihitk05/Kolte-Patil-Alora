function interior() {
  document.getElementById("interiors-gallery").style.display = "flex";
  document.getElementById("interiors-gallery").style.justifyContent =
    "space-evenly";
  document.getElementById("exteriors-gallery").style.display = "none";
  document.getElementById("amenities-gallery").style.display = "none";
  document.getElementById("layout-gallery").style.display = "none";
}
function exterior() {
  document.getElementById("interiors-gallery").style.display = "none";
  document.getElementById("exteriors-gallery").style.display = "flex";
  document.getElementById("exteriors-gallery").style.justifyContent =
    "space-evenly";
  document.getElementById("amenities-gallery").style.display = "none";
  document.getElementById("layout-gallery").style.display = "none";
}
function amenities() {
  document.getElementById("interiors-gallery").style.display = "none";
  document.getElementById("exteriors-gallery").style.display = "none";
  document.getElementById("amenities-gallery").style.display = "flex";
  document.getElementById("amenities-gallery").style.justifyContent =
    "space-evenly";
  document.getElementById("layout-gallery").style.display = "none";
}
function layout() {
  document.getElementById("interiors-gallery").style.display = "none";
  document.getElementById("exteriors-gallery").style.display = "none";
  document.getElementById("amenities-gallery").style.display = "none";
  document.getElementById("layout-gallery").style.display = "flex";
  document.getElementById("layout-gallery").style.justifyContent = "center";
}


function interior_mob() {
  document.getElementById("interiors-gallery-mob").style.display = "flex";
  document.getElementById("interiors-gallery-mob").style.justifyContent =
    "space-evenly";
  document.getElementById("exteriors-gallery-mob").style.display = "none";
  document.getElementById("amenities-gallery-mob").style.display = "none";
  document.getElementById("layout-gallery-mob").style.display = "none";
}
function exterior_mob() {
  document.getElementById("interiors-gallery-mob").style.display = "none";
  document.getElementById("exteriors-gallery-mob").style.display = "flex";
  document.getElementById("exteriors-gallery-mob").style.justifyContent =
    "space-evenly";
  document.getElementById("amenities-gallery-mob").style.display = "none";
  document.getElementById("layout-gallery-mob").style.display = "none";
}
function amenities_mob() {
  document.getElementById("interiors-gallery-mob").style.display = "none";
  document.getElementById("exteriors-gallery-mob").style.display = "none";
  document.getElementById("amenities-gallery-mob").style.display = "flex";
  document.getElementById("amenities-gallery-mob").style.justifyContent =
    "space-evenly";
  document.getElementById("layout-gallery-mob").style.display = "none";
}
function layout_mob() {
  document.getElementById("interiors-gallery-mob").style.display = "none";
  document.getElementById("exteriors-gallery-mob").style.display = "none";
  document.getElementById("amenities-gallery-mob").style.display = "none";
  document.getElementById("layout-gallery-mob").style.display = "flex";
  document.getElementById("layout-gallery-mob").style.justifyContent = "center";
}


