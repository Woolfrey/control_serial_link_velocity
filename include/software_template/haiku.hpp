/**
 * @file    example_haiku.hpp
 * @author  Jon Woolfrey
 * @email   jonathan.woolfrey@gmail.com
 * @date    Month Year
 * @version 1.0
 * @brief   A haiku is a poem consisting of 3 lines, with 5, 7, and then 5 syllables respectively.
 *
 * @details This header files is an example of what should be used in a C++ software library.
 * 
 * @copyright Copyright (c) Year Jon Woolfrey
 * 
 * @license GNU General Public License V3
 * 
 * @see https://github.com/Woolfrey/
 */
 
#ifndef EXAMPLE_HAIKU_H
#define EXAMPLE_HAIKU_H

#include <iostream>                                                                                 // std::cout
#include <string>                                                                                   // std::string


namespace template_class{
 
 /**
  * @brief Header file for a haiku class.
  */
class Haiku
{
    public:
        
        /**
         * @brief This is an empty constructor.
         */
        Haiku() {}
        
        /**
         * @brief Read a haiku.
         */
        static
        void
        read();
        
        /**
         * @brief Get a single line.
         * @param lineNumber Do I need to explain this?
         */
        static
        std::string
        get_line(const unsigned int &lineNumber);
};

} // namespace

#endif
