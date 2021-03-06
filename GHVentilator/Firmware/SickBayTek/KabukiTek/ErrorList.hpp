/** Kabuki Tek @version 0.x
@link  https://github.com/KabukiStarship/KabukiTek.git
@file  /ErrorList.hpp
@author  Cale McCollough <https://cale-mccollough.github.io>
@license Copyright 2020 (C) Kabuki Starship <kabukistarship.com>.
This Source Code Form is subject to the terms of the Mozilla Public License, 
v. 2.0. If a copy of the MPL was not distributed with this file, you can obtain 
one at <https://mozilla.org/MPL/2.0/>. */
#pragma once
#include <_Config.h>
namespace _ {

/* An array of error strings.
@code
ErrorList<5> Errors;

@endcode
*/
template<unsigned int ErrorCountMax>
class ErrorList {
  public:

    /* Default simple constructor. */
    ErrorList ()
    :   ErrorCount (0) {
        /// Nothing to do here! :-)
    }

    /* Clears the error list. */
    void Clears () { ErrorCount = 0; }

    /* Gets the number of Errors. */
    unsigned int ErrorCountGet () { return ErrorCount; }

    /* Reports an error with the given message. */
    void Report (const char* Error) {
        if (ErrorCount >= ErrorCountMax) return;
        Errors[ErrorCount++] = Error;
        return this;
    }

    /* Reports an error with the given message. */
    ErrorList& operator += (const char* Error) {
        Report (Error);
        return this;
    }

    virtual void Print () {
        for (int i = 0; i < ErrorCount; ++i)
            printf ("\r\n%s", Errors[i]);
    }

    /* Returns the list of Errors. */
    const char* ErrorsGet () { return Errors; }

  private:

    unsigned int ErrorCount;

    const char* Errors[ErrorCountMax];
};

}   //< namespace _
