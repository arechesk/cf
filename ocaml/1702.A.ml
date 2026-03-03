(* Solution without any external library, using only string manipulation.
   The result is built directly from the string representation to avoid
   the need for big integers. *)

let drop_leading_zeros s =
  let len = String.length s in
  let rec aux i =
    if i >= len then ""                (* all zeros *)
    else if s.[i] <> '0' then String.sub s i (len - i)
    else aux (i + 1)
  in aux 0

let () =
  let t = int_of_string (input_line stdin) in
  for _ = 1 to t do
    let s = input_line stdin in
    (* Special case: the only input that can lead to a negative result *)
    if s = "0" then
      print_endline "-1"
    else
      let len = String.length s in
      let first = s.[0] in
      let rest =
        if len > 1 then String.sub s 1 (len - 1)
        else ""
      in
      if first = '1' then
        (* result is just the tail, with leading zeros removed *)
        let trimmed = drop_leading_zeros rest in
        print_endline (if trimmed = "" then "0" else trimmed)
      else
        (* first digit is > 1: decrease it by one and keep the tail *)
        let new_first = Char.chr (Char.code first - 1) in
        print_endline (String.make 1 new_first ^ rest)
  done
