/** mbedBug @version 0.x
@link    https://github.com/KabukiStarship/mbedbug.git
@file    /morse_code.h
@author  Cale McCollough <https://cale-mccollough.github.io>
@license Copyright 2016-20 (C) Kabuki Starship <kabukistarship.com>; all rights 
reserved (R). This Source Code Form is subject to the terms of the Mozilla 
Public License, v. 2.0. If a copy of the MPL was not distributed with this file,
You can obtain one at <https://mozilla.org/MPL/2.0/>. */
#pragma once
#ifndef MBEDBUG_MORSECODE_DECL
#define MBEDBUG_MORSECODE_DECL
namespace mbedbug {

/* Gets the Morse code for the given char. */
const char* CodeMorseEncode (char Value);

}   //< namespace mbedbug
#endif
