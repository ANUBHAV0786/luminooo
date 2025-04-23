https://www.youtube.com/watch?v=H_4BknKaAxc

we will try to finalize our Home page template that we have started in our step 11


================================================================================================
================================================================================================
STEP 12:: We will add templates like 
                1. Footer
                2. Testimonials
================================================================================================
================================================================================================
Open Home.components.js file 
        like we have created cards for Latest and Popular courses 

        Here we will create card for our popular teachers


and we have added same cards for teachers and changes placement of words only

-=================================================================================================


STEP 12 : Now we're going to add some bootstrap templates

step 12.A  Adding FOOTER 

      12.a.1  we will create our Footer.components.js file 

        12.a.2 then create the boiler plate code for footer

                        function Footer() {
                                    return (
                                        </footer>
                                        
                                    </footer>
                                    );
                                }
        
                        export default Footer;

        12.a.3 now we make changes inside our footer tag as we require.


        12.a.4 after that we import our footer in our main.component.js



  

STEP 12.B  Adding TESTIMONIALS

    12.b.1 we will NOT create a component file for  Testimonials as we are going to use it only on our Home Page

            so we will go to bootstrap and search for the Crousel as we're going to  add slide for our testimonils

            copy the carousel code 

    12.b.2 go to Home.component.js and add the copied code after the Featured Teachers

    12.b.3 now goto bootstrap again and look for the  Blockquotes and copy the Alignment code and 

    12.b.4 now paste blockquotes codes within the carousel item replace the <img> tag line with the copied code 

                this will create our testimonial at the bottom of the page which can be toggeled through button and it will toggle itself 


