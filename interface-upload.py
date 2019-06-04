Framed[Grid[{
{Text[Style["Which Harry Potter Character Are You?", Bold, 18]]},
{Dynamic[image]},
{Text[Style[Dynamic[character], Bold, 18]],
FileNameSetter[Dynamic[file], Appearance -> "Select New Image"]},
{Text[Style[Dynamic[probabilities], 14]],
Button["Classify Image",
image = Import[file];
character = potter[image];
probabilities = Normal[potter[image, "Probabilities"]]]}}],
FrameStyle -> Thick]
