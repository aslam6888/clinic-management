import { Box, Flex, Text } from '@chakra-ui/react'
import React from 'react'
import { FiBarChart2, FiCalendar } from "react-icons/fi";
import { FaUserDoctor } from "react-icons/fa6";
import { FaHospitalUser } from "react-icons/fa";
import { TbReport } from "react-icons/tb";
import { Link } from 'react-router-dom';


function SideNav() {
    var routes = [
        { name: 'Dashboard', url: '/', icon: FiBarChart2 },
        { name: 'Appointments', url: '/', icon: FiCalendar },
        { name: 'Doctors', url: '/doctors', icon: FaUserDoctor },
        { name: 'Patients', url: '/', icon: FaHospitalUser },
        { name: 'Reports', url: '/', icon: TbReport }
    ]
    return (
        <Flex width={304} backgroundColor={'white'} h={'92vh'} flexDir={'column'} justifyContent={'space-between'} overflow={'hidden'}>
            <Box>
                <Box mt={2} p={2}>
                    {routes.map((val, index) => {
                        return (
                            <Link to={val.url}>
                                <Flex alignItems={'center'} p={3} className='sidenav-item'>
                                    <div><val.icon size={20} /></div> <div><Text fontSize={17} fontWeight={500} ml={3}>{val.name} </Text></div>
                                </Flex>
                            </Link>
                        )
                    })}
                </Box>
            </Box>

            <Box>A</Box>
        </Flex>
    )
}

export default SideNav