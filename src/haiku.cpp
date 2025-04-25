/**
 * @file    haiku.cpp
 * @author  Jon Woolfrey
 * @email   jonathan.woolfrey@gmail.com
 * @date    Month Year
 * @version 1.0
 * @brief   Source files for the Haiku class.
 *
 * @details This header files is an example of what should be used in a C++ software library.
 * 
 * @copyright Copyright (c) Year Jon Woolfrey
 * 
 * @license GNU General Public License V3
 * 
 * @see https://github.com/Woolfrey/
 */
 
#include <software_template/haiku.hpp>

namespace template_class {
 
  ////////////////////////////////////////////////////////////////////////////////////////////////////
 //                                     Read the full haiku                                        //
////////////////////////////////////////////////////////////////////////////////////////////////////
void
Haiku::read()
{
    for (unsigned int i = 1; i < 4; ++i) std::cout << get_line(i) << "\n";
}
   
  ////////////////////////////////////////////////////////////////////////////////////////////////////
 //                                Get a single line of the haiku                                  //
////////////////////////////////////////////////////////////////////////////////////////////////////        
std::string
Haiku::get_line(const unsigned int &lineNumber)
{
    switch (lineNumber)
    {
        case 1:
        {
            return "Worker bees can leave.";
            break;
        }
        case 2:
        {
            return "Even drones can fly away.";
            break;
        }
        case 3:
        {
            return "The Queen is their slave.";
            break;
        }
        default:
        {
            return "FLAGRANT SYSTEM ERROR.";
        }
    }
}

} // template_class
  
