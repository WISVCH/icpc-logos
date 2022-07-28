#!/usr/bin/env bash

sizes=(64 256)

joinByChar() {
  local IFS="$1"
  shift
  echo "$*"
}

organizations=$(cat organizations.json | jq -r .\[\].id)

for i in $organizations; do
    svg="$(pwd)/logos/$i.svg"

    if [ -f "$svg" ]; then
      echo "exporting ${i}"
    else
      echo "Can't find $svg"
      continue
    fi

    tmpfile=$(mktemp /tmp/svg_logos.XXXXXX)
    cp $svg $tmpfile

    if [[ "${i::1}" == "U" ]]; then
      circle=1
    else
      circle=0
    fi

    exports=()
    exports+=("select:black;selection-hide")
    exports+=("select:background_x5F_circle;selection-`if [[ "$circle" -eq 1 ]]; then echo 'un'; fi`hide;select:background_x5F_rectangle;selection-`if [[ "$circle" -eq 0 ]]; then echo 'un'; fi`hide")
    # If I only do it once it didn't work
    exports+=("select:background_x5F_circle;selection-`if [[ "$circle" -eq 1 ]]; then echo 'un'; fi`hide;select:background_x5F_rectangle;selection-`if [[ "$circle" -eq 0 ]]; then echo 'un'; fi`hide")


    for s in ${sizes[@]}; do
        mkdir -p "out/background/$s"
        exportFilename="out/background/$s/$i.png"
        exports+=("export-type:png;export-background-opacity:0;export-width:$s;export-filename:$exportFilename;export-do")
    done

    exports+=("select:background_x5F_circle;selection-hide;select:background_x5F_rectangle;selection-hide")

    for s in ${sizes[@]}; do
        mkdir -p "out/transparent/$s"
        exportFilename="out/transparent/$s/$i.png"
        exports+=("export-type:png;export-background-opacity:0;export-width:$s;export-filename:$exportFilename;export-do")
    done

    inkscape --actions="`joinByChar ';' ${exports[@]}`" $tmpfile
    rm "$tmpfile"
done
