import SupportAgentIcon from "@mui/icons-material/SupportAgent";
import Diversity3Icon from "@mui/icons-material/Diversity3";
import HandshakeIcon from "@mui/icons-material/Handshake";
import HealthAndSafetyIcon from "@mui/icons-material/HealthAndSafety";
import LocalShippingIcon from "@mui/icons-material/LocalShipping";
import VolunteerActivismIcon from '@mui/icons-material/VolunteerActivism';

export const LeftBarStatic = [
  {
    id: "agent",
    title: "Agent",
    icon: <SupportAgentIcon />,
    link: "/agents"
  },
  {
    id: "referral",
    title: "Referral",
    icon: <HealthAndSafetyIcon />,
    link: "/referrals"
  },
  {
    id: "client",
    title: "Client",
    icon: < Diversity3Icon />,
    link: "/clients"
  },
  {
    id: "donor",
    title: "Donor",
    icon: <HandshakeIcon />,
    link: "/donors"
  },
  {
    id: "donation",
    title: "Donation",
    icon: <VolunteerActivismIcon />,
    link: "/donations"
  },
  {
    id: "delivery",
    title: "Delivery",
    icon: <LocalShippingIcon />,
    link: "/deliveries"
  }
]
