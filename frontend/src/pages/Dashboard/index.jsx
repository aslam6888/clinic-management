import { Box, Card, CardBody, Grid, Text, Breadcrumb, BreadcrumbItem, BreadcrumbLink } from '@chakra-ui/react'
import React from 'react'
import { BiChevronsRight } from "react-icons/bi";
import Chart from './LineChart';
function Dashbaord() {
    return (
        <>
            <Breadcrumb spacing='8px' separator={<BiChevronsRight color='gray.500' />}>
                <BreadcrumbItem>
                    <BreadcrumbLink href='#'>Home</BreadcrumbLink>
                </BreadcrumbItem>

                <BreadcrumbItem>
                    <BreadcrumbLink href='#'>About</BreadcrumbLink>
                </BreadcrumbItem>

                <BreadcrumbItem isCurrentPage>
                    <BreadcrumbLink href='#'>Contact</BreadcrumbLink>
                </BreadcrumbItem>
            </Breadcrumb>

            <Box mt={5}>
                <Text fontSize={22} fontWeight={600}>Dashboard Overview</Text>
            </Box>
            <Grid templateColumns='repeat(4, 1fr)' gap={6} mt={4}>
                <Card>
                    <CardBody>
                        <Text fontSize={20}>Total Patients</Text>
                        <Text fontSize={30}>672</Text>
                    </CardBody>
                </Card>
                <Card>
                    <CardBody>
                        <Text fontSize={20}>Patients Today</Text>
                        <Text fontSize={30}>2</Text>
                    </CardBody>
                </Card>
                <Card>
                    <CardBody>
                        <Text fontSize={20}>Appointments Today</Text>
                        <Text fontSize={30}>45</Text>
                    </CardBody>
                </Card>
                <Card>
                    <CardBody>
                        <Text fontSize={20}>Patients Today</Text>
                        <Text fontSize={30}>2</Text>
                    </CardBody>
                </Card>
            </Grid>
            <Card>
            <Chart/>
            </Card>
                
            


        </>
    )
}

export default Dashbaord