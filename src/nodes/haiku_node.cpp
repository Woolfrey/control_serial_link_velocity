/**
 * @file    haiku_node.cpp
 * @author  Jon Woolfrey
 * @email   jonathan.woolfrey@gmail.com
 * @date    Month Year
 * @version 1.0
 * @brief   This is an example of an executable (ROS2 style).
 *
 * @details When executed, reads an haiku.
 * 
 * @copyright Copyright (c) Year Jon Woolfrey
 * 
 * @license GNU General Public License V3
 * 
 * @see https://github.com/Woolfrey/
 */
 
#include <software_template/haiku.hpp>

int main(int argc, char *argv[])
{
    template_class::Haiku::read();
    
    return 0;                                                                                       // No problems with main
}
