
import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Hero from './components/Hero';
import AboutSection from './components/AboutSection';
import ServicesSection from './components/ServicesSection';
import TestimonialsSection from './components/TestimonialsSection';
import ContactSection from './components/ContactSection';
import Footer from './components/Footer';
import ServiceSelectionModal from './components/ServiceSelectionModal';
import { ndisContent, agedCareContent, Content } from './components/content';
import { ndisTheme, agedCareTheme, Theme } from './components/themes';

type ServiceType = 'ndis' | 'agedCare';

const App: React.FC = () => {
  const [service, setService] = useState<ServiceType | null>(null);
  const [content, setContent] = useState<Content>(ndisContent);
  const [isModalOpen, setIsModalOpen] = useState(true);

  useEffect(() => {
    const theme = service === 'agedCare' ? agedCareTheme : ndisTheme;
    const root = document.documentElement;
    Object.entries(theme).forEach(([key, value]) => {
      root.style.setProperty(key, value);
    });

    setContent(service === 'agedCare' ? agedCareContent : ndisContent);
  }, [service]);

  const handleServiceSelect = (selectedService: ServiceType) => {
    setService(selectedService);
    setIsModalOpen(false);
  };

  if (!service) {
    return <ServiceSelectionModal onSelect={handleServiceSelect} />;
  }

  return (
    <div className="bg-brand-bg font-sans text-brand-text">
      <Header />
      <main>
        <Hero content={content.hero} />
        <AboutSection content={content.about} />
        <ServicesSection content={content.services} />
        <TestimonialsSection content={content.testimonials} />
        <ContactSection />
      </main>
      <Footer />
    </div>
  );
};

export default App;