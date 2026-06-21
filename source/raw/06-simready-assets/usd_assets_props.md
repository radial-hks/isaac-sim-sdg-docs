---
url: https://docs.isaacsim.omniverse.nvidia.com/latest/assets/usd_assets_props.html
title: "Props"
section: "资产库"
module: "06-simready-assets"
checksum: "f8c850a2c045e234"
fetched: "2026-06-21T13:40:29"
---

* [Isaac Sim Assets](usd_assets_overview.html)
* Prop Assets

[Is this page helpful?](https://surveys.hotjar.com/4904bf71-6484-47a7-83ff-4715cceabdb5)

# Prop Assets

## Characters

Listed below are a few characters available in Isaac-Sim, located in the Content Browser inside the `Isaac Sim` folder.

### Police Man

Male character in police uniform with retargeted skeleton.

`People/Characters/original_male_adult_police_04/male_adult_police_04.usd` in the Content Browser.

### Male Doctor

Male character in doctor uniform with retargeted skeleton.

`People/Characters/origial_male_adult_medical_01/male_adult_medical_01.usd` in the Content Browser.

### Police Woman

Female character in police uniform with retargeted skeleton.

`People/Characters/female_adult_police_02/female_adult_police_02.usd` in the Content Browser.

### Construction Worker

Male character in construction uniform with retargeted skeleton.

`People/Characters/origial_male_adult_construction_03/male_adult_construction_03.usd` in the Content Browser.

Note

User can change a character’s clothing color by modifying material’s `Property -> Material and Shader` value

Here is an example of how to change male\_adult\_construction\_03’s safety hat’s color

* First, expand the character on the stage menu and navigate to their `Looks` folder. Example - `/World/male_adult_construction_03/Looks`.
* Next, select your target material (Example - `opaque__plastic__hardhat`) and change material’s `Property -> Material and Shader -> Albedo -> Color Tint` value to adjust character’s color.

### April Tags

We provide a simple mdl material that can index into a April Tag mosaic image.

To use, add the material to your stage using `Create->April Tag->`

Then create a mesh cube using `Create->Mesh->Cube` and assign the AprilTag material to that prim

The material has the following parameters which need to be configured:

* `Mosaic texture` The path to the texture that contains the grid of April tag images
* `Tag Size` The width/height of the tag in pixels
* `Tags Per Row` The number of tag images per row in the mosaic
* `Spacing` The number of padding pixels between each tag image
* `Tag ID` The index of the tag to use.

The figure below shows example usage using `tag36h11.png`,
after manually creating the mesh cube and assigning the material as described above.

On this page

* [Characters](#characters)
  + [Police Man](#police-man)
  + [Male Doctor](#male-doctor)
  + [Police Woman](#police-woman)
  + [Construction Worker](#construction-worker)
  + [April Tags](#april-tags)