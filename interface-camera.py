Framed[Grid[{
{Text[Style["Which Harry Potter Character Are You?", Bold, 18]]},
{Dynamic[image]},
{Text[Style[Dynamic[character], Bold, 18]],
Button["New Photo",
image = CurrentImage[ImageSize -> 350];
character = potter[image];
probabilities = Normal[potter[image, "Probabilities"]]]},
{Text[Style[Dynamic[probabilities], 14]]}}], FrameStyle -> Thick]
