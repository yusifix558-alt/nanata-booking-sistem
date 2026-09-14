import BookingWizard from "@/components/booking/BookingWizard";

export const metadata = {
  title: "Booking | Namata Studio",
  description: "Jadwalkan treatment nail art dan eyelash kamu dengan mudah.",
};

export default function BookingPage() {
  return (
    <div className="min-h-screen pt-24 pb-12 px-4 sm:px-6 bg-paper flex flex-col justify-start">
      <div className="max-w-3xl mx-auto mb-8 sm:mb-12 text-center mt-4">
        <h1 className="font-editorial text-4xl sm:text-6xl font-bold text-dark mb-4">Reservation.</h1>
        <p className="text-dark/70 text-xs sm:text-sm uppercase tracking-widest hidden sm:block">Atur jadwal treatment kamu dengan para artist kami.</p>
      </div>
      
      <BookingWizard />
    </div>
  );
}
